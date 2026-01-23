from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
from django.conf import settings

def _get_font(size):
    """Türkçe karakter destekli Bold font bulma mantığı"""
    # Docker (Linux) ortamında daha belirgin olan Bold versiyonları önceliklendirdik
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in font_paths:
        if os.path.exists(path):
            return ImageFont.truetype(path, size=size)
    
    # Font bulunamazsa sistemin default fontunu döner (size burada çalışmaz, küçüktür)
    return ImageFont.load_default()

def apply_watermark(image_path):
    if not getattr(settings, "WATERMARK_ENABLED", False):
        return
    
    if not image_path or not os.path.exists(image_path):
        return

    try:
        # Resmi açarken formatını kaybetmemek için orijinal nesneyi saklıyoruz
        with Image.open(image_path) as im:
            original_format = im.format
            # EXIF bilgilerine göre yönü düzelt (Yan yüklenen resimler için)
            im = ImageOps.exif_transpose(im)
            
            # Şeffaf katman desteği için RGBA'ya çevir
            base = im.convert("RGBA")
            W, H = base.size
            
            # Yazı için tamamen şeffaf bir katman oluştur
            overlay = Image.new("RGBA", (W, H), (255, 255, 255, 0))
            draw = ImageDraw.Draw(overlay)
            
            # Dinamik font boyutu: Genişliğin %8 ile %10 arası idealdir.
            # %12 yaparak biraz daha büyüttüm ki iyice belirgin olsun.
            fs = int(W * 0.12)
            font = _get_font(fs)
            text = "egitimbul.io"
            
            # Metin boyutunu ölç (bbox: left, top, right, bottom)
            bbox = draw.textbbox((0, 0), text, font=font)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]
            
            # Yazıyı tam ortaya konumlandır
            # Şeffaflık (fill) değerini 128'den 160'a çekerek biraz daha görünür yaptım.
            draw.text(((W - tw) // 2, (H - th) // 2), text, font=font, fill=(255, 255, 255, 160))
            
            # Orijinal resim ile yazı katmanını birleştir
            out = Image.alpha_composite(base, overlay)
            
            # Kayıt işlemi
            if original_format in ["JPEG", "JPG"]:
                out = out.convert("RGB")
                # Kaliteyi %95 yaparak bozulmayı önlüyoruz
                out.save(image_path, "JPEG", quality=95, optimize=True)
            else:
                # PNG veya diğer formatlarda orijinal formatı koru
                out.save(image_path, original_format)
                
    except Exception as e:
        print(f"Watermark Error: {e}")