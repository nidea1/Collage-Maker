from django.shortcuts import render
from django.http import HttpResponse
from .forms import CollageForm
from PIL import Image

def index(request):
    if request.method == 'POST':
        form = CollageForm(request.POST, request.FILES)
        if form.is_valid():
            # retrieving files from the form
            images = request.FILES.getlist('images')

            # images are listing
            image_list = [Image.open(img) for img in images]
            
            # padding value for spacing between images
            padding = 20

            #take the dimensions of the images and calculate the collage size
            widths,heights = zip(*(i.size for i in image_list))
            width = sum(widths) + ((len(image_list)) * padding) + padding
            height = max(heights) + (2 * padding)
            

            # selecting style
            style = form.cleaned_data['style']

            # collage is made according to the selected style
            if style == '1':
                collage = Image.new('RGB', (width,height), (255,255,255))
                x_offset = padding
                for img in image_list:
                    y_offset = (height - img.size[1]) // 2
                    collage.paste(img, (x_offset, y_offset))
                    x_offset += img.size[0] + padding
            else:
                width = sum(widths) // 2 + ((len(image_list)) // 2 * padding) + padding
                height = max(heights) * 2 + padding * 3
                collage = Image.new('RGB', (width,height), (255,255,255))
                x_offset = padding
                half = len(image_list) // 2

                for img in image_list[:half]:
                    y_offset = (height // 2 - img.size[1]) - padding // 2
                    collage.paste(img, (x_offset, y_offset))
                    x_offset += img.size[0] + padding

                x_offset = padding
                for img in image_list[half:]:
                    y_offset = (height - img.size[1]) - padding 
                    collage.paste(img, (x_offset, y_offset))
                    x_offset += img.size[0] + padding
            
            # the collage is saved and presented to the user
            collage.save('collage.jpg')
            with open('collage.jpg', 'rb') as f:
                response = f.read()
            
            return HttpResponse(response, content_type='image/jpeg')       

    else:
        form = CollageForm()
    return render(request, 'index.html', {'form': form})