from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill

class DynamicSeoSpec(ImageSpec):
    def __init__(self, **kwargs):
        # 1. Bize lazım olan özel argümanları kwargs içinden çekip alalım (pop)
        # Böylece super()'a gitmezler ve hata vermezler.
        self.custom_context = {
            'width': kwargs.pop('width', 800),
            'height': kwargs.pop('height', 600),
            'format': kwargs.pop('format', 'WEBP'),
            'quality': kwargs.pop('quality', 80),
        }
        
        # 2. Artık kwargs içinde sadece ImageSpec'in tanıdığı (source gibi) 
        # argümanlar kaldı. Güvenle super() çağrılabilir.
        super(DynamicSeoSpec, self).__init__(**kwargs)

    @property
    def format(self):
        fmt = str(self.custom_context.get('format')).upper()
        return 'JPEG' if fmt == 'JPG' else fmt

    @property
    def options(self):
        return {'quality': int(self.custom_context.get('quality'))}

    @property
    def processors(self):
        width = int(self.custom_context.get('width'))
        height = int(self.custom_context.get('height'))
        return [ResizeToFill(width, height, upscale=False)]

register.generator('core:seo_image', DynamicSeoSpec)