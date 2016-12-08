# models.py (the database tables)


from django.db import models
from django.core.urlresolvers import reverse


class User(models.Model):
    CREATED = 'created'
    VALIDATED = 'validated'
    DELETED = 'deleted'
    status_choice_s = (
        (CREATED, 'Created'),
        (VALIDATED, 'Validated'),
        (DELETED, 'Deleted'),
    )
    ANNOUNCER = 'announcer'
    NORMAL_ADMIN = 'normal_admin'
    SUPER_ADMIN = 'super_admin'
    role_choice_s = (
        (ANNOUNCER, 'Announcer'),
        (NORMAL_ADMIN, 'Normal Admin'),
        (SUPER_ADMIN, 'Super Admin'),
    )

    status = models.CharField(max_length=140, choices=status_choice_s, default=CREATED)
    password_hash = models.CharField(max_length=140)
    email = models.EmailField(max_length=140, unique=True)
    # display_name = models.CharField(max_length=140, unique=True)
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    role = models.CharField(max_length=140, choices=role_choice_s, default=ANNOUNCER)
    address = models.CharField(max_length=140)
    city = models.CharField(max_length=140)
    county = models.CharField(max_length=140)
    phone_number = models.CharField(max_length=140)
    birth = models.CharField(max_length=140)
    reg_date = models.DateTimeField('date registered')

    def get_absolute_url(self):
        return reverse('main:profile', kwargs={'pk': self.pk})  # form inserted into db, then redirect to this url.

    def __str__(self):
        return self.email


class Announce(models.Model):
    # status
    DRAFT_STARTED = 'draft_started'
    DRAFT_FINISHED = 'draft_finished'
    CREATED = 'created'
    PUBLISHED = 'published'
    EXPIRED_AUTO = 'expired_auto'
    EXPIRED_MANUAL = 'expired_manual'
    DELETED = 'deleted'
    REPLACED = 'replaced'
    status_choice_s = (
        (DRAFT_STARTED, 'Draft Started'),
        (DRAFT_FINISHED, 'Draft Finished'),
        (CREATED, 'Created'),
        (PUBLISHED, 'Published'),
        (EXPIRED_AUTO, 'Expired Auto'),
        (EXPIRED_MANUAL, 'Expired Manual'),
        (DELETED, 'deleted'),
        (REPLACED, 'replaced'),
    )
    # type
    SMALL_CAR = 'small_car'
    MEDIUM_CAR = 'medium_car'
    LARGE_CAR = 'large_car'
    EXECUTIVE_CAR = 'executive_car'
    LUXURY_CAR = 'luxury_car'
    SPORTS_COUPES = 'sports_coupes'
    MULTIPURPOSE_CAR = 'multipurpose_car'
    SUV = 'suv'
    FAMILY_BUS = 'family_bus'
    type_choice_s = (
        (SMALL_CAR, 'Small Car'),
        (MEDIUM_CAR, 'Medium Car'),
        (LARGE_CAR, 'Large Car'),
        (EXECUTIVE_CAR, 'Executive Car'),
        (LUXURY_CAR, 'Luxury Car'),
        (SPORTS_COUPES, 'Sports Coupes'),
        (MULTIPURPOSE_CAR, 'Multipurpose Car'),
        (SUV, 'SUV'),
        (FAMILY_BUS, 'Family Bus'),
    )
    # gear box
    AUTOMATIC = 'automatic'
    MANUAL = 'manual'
    gear_box_choice_s = (
        (AUTOMATIC, 'Automatic'),
        (MANUAL, 'Manual'),
    )
    # fuel
    PETROL = 'petrol'
    DIESEL = 'diesel'
    ELECTRONIC = 'electronic'
    HYBRID = 'hybrid'
    fuel_choice_s = (
        (PETROL,  'Petrol'),
        (DIESEL,  'Diesel'),
        (ELECTRONIC,  'Electronic'),
        (HYBRID,  'Hybrid'),
    )
    # verified_media
    VERIFIED_MEDIA_NO = 0
    VERIFIED_MEDIA_YES = 1
    verified_media_choice_s = (
        (VERIFIED_MEDIA_NO, 'Nej'),
        (VERIFIED_MEDIA_YES, 'Ja'),
    )

    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=140)
    status = models.CharField(max_length=140, choices=status_choice_s, default=CREATED)
    location = models.CharField(max_length=140, default='DEFAULT VALUE')
    brand = models.CharField(max_length=140)
    model = models.CharField(max_length=140)
    model_year = models.IntegerField()
    mileage = models.IntegerField()
    type = models.CharField(max_length=140, choices=type_choice_s, default=SUV)
    gear_box = models.CharField(max_length=140, choices=gear_box_choice_s, default=AUTOMATIC)
    fuel = models.CharField(max_length=140, choices=fuel_choice_s, default=PETROL)
    description = models.CharField(max_length=2048)
    price = models.IntegerField()
    submit_time = models.DateTimeField('submit time')
    publish_time = models.DateTimeField()
    verified_media = models.IntegerField(choices=verified_media_choice_s, default=VERIFIED_MEDIA_NO)
    last_update_time = models.DateTimeField()
    expire_time = models.DateTimeField()
    filename = models.CharField(max_length=140, default='20160904/1.jpg')


    def get_absolute_url(self):
        return reverse('main:cars-detail', kwargs={'pk': self.pk})  # form inserted into db, then redirect to this url.

    def __str__(self):
        return self.title


class Media(models.Model):
    IMAGE = 'image'
    YOUTUBE = 'youtube'
    AUDIO = 'audio'
    type_choice_s = (
        (IMAGE, 'Image'),
        (YOUTUBE, 'Video'),
        (AUDIO, 'Audio'),
    )

    announce_id = models.ForeignKey(Announce, on_delete=models.CASCADE)
    type = models.CharField(max_length=140, choices=type_choice_s, default=IMAGE)
    filename = models.CharField(max_length=140, default='')

    def __str__(self):
        return self.announce_id
