def readFile(filename):
    with open(filename) as f:
        content = f.read().splitlines()
    nr_of_photos = content.pop(0)
    ready_photos = []
    vertical_photos = []
    for i, con in enumerate(content):
        photo_args = con.split(' ')
        ori = photo_args[0]
        p = Photo(str(i), ori, photo_args[1], photo_args[2:])
        if ori == 'V':
            vertical_photos.append(p)
        else:
            ready_photos.append(p)
    return nr_of_photos, ready_photos, vertical_photos

class Photo:
    def __init__(self, id, ori, nr_of_tags, tags):
        self.id = id
        self.ori = ori
        self.nr_of_tags = nr_of_tags
        self.tags = set(tags)

    def calcPoint(self, other):
        overlapping_tags = len(self.tags & other.tags)
        unique_tag_photo_1 = len(self.tags - other.tags)
        unique_tag_photo_2 = len(other.tags - self.tags)
        return min(overlapping_tags, unique_tag_photo_1, unique_tag_photo_2)


# nr_of_photos, ready_photos, vertical_photos = readFile('D:\\Google Hashcode\\PhotoSlideshow\\a_example.txt')
# nr_of_photos, ready_photos, vertical_photos = readFile('D:\\Google Hashcode\\PhotoSlideshow\\b_lovely_landscapes.txt')
nr_of_photos, ready_photos, vertical_photos = readFile('D:\\Google Hashcode\\PhotoSlideshow\\c_memorable_moments.txt')
# nr_of_photos, ready_photos, vertical_photos = readFile('D:\\Google Hashcode\\PhotoSlideshow\\d_pet_pictures.txt')
# nr_of_photos, ready_photos, vertical_photos = readFile('D:\\Google Hashcode\\PhotoSlideshow\\e_shiny_selfies.txt')
# print(photos[1].nr_of_tags)
# print(photos[1].calcPoint(photos[2]))
# Combine vertical photos
for i in range(len(vertical_photos)//2):
    vp1 = vertical_photos[i*2]
    vp2 = vertical_photos[i*2+1]
    combined_tags = vp1.tags | vp2.tags
    photo = Photo(vp1.id + ' ' + vp2.id, 'C', len(combined_tags), combined_tags)
    ready_photos.append(photo)

slideshow = []
last_total_score = 0;
new_total_score = 0;
currentPhoto = ready_photos.pop(0)
while(len(ready_photos) > 0):
    max_score = 0
    for i, photo in enumerate(ready_photos):
        score = currentPhoto.calcPoint(photo)
        if score>0:
            new_total_score += score
            photo2 = ready_photos.pop(i)
            if slideshow and slideshow[-1] == currentPhoto:
                slideshow += [photo2]
            else:
                slideshow += [currentPhoto, photo2]
            currentPhoto = photo2
    if(last_total_score == new_total_score):
        currentPhoto = ready_photos.pop()
    else:
        last_total_score = new_total_score

# for photo in slideshow:
#     print('ID: ', photo.id, ', Tags: ', photo.tags)
print(new_total_score)


