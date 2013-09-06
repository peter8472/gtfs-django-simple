# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
import django.utils.timezone

class Agency(models.Model):
    agency_id = models.CharField(max_length=300, blank=True)
    agency_name = models.CharField(max_length=765, blank=True)
    agency_url = models.CharField(max_length=765, blank=True)
    agency_timezone = models.CharField(max_length=300, blank=True)
    agency_phone = models.CharField(max_length=75, blank=True)
    agency_fare_url = models.CharField(max_length=1500, blank=True)
    agency_lang = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'agency'

class NowManager(models.Manager):
    def get_query_set(self):
        return super(NowManager, self).get_query_set().filter(
	    start_date__lte=django.utils.timezone.now()).filter(
	    end_date__gte=django.utils.timezone.now())

class Calendar(models.Model):
    service_id = models.CharField(primary_key=True,max_length=45, blank=True)
    service_name = models.CharField(max_length=300, blank=True)
    monday = models.IntegerField(null=True, blank=True)
    tuesday = models.IntegerField(null=True, blank=True)
    wednesday = models.IntegerField(null=True, blank=True)
    thursday = models.IntegerField(null=True, blank=True)
    friday = models.IntegerField(null=True, blank=True)
    saturday = models.IntegerField(null=True, blank=True)
    sunday = models.IntegerField(null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    objects = models.Manager()
    class Meta:
        db_table = u'calendar'
    nowmanager = NowManager()
    def getService(self):
	return self.service_id

class CalendarDates(models.Model):
    service_id = models.CharField(max_length=45, blank=True)
    date = models.DateTimeField()
    exception_type = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'calendar_dates'


class FareAttributes(models.Model):
    agency_id = models.CharField(max_length=300, blank=True)
    fare_id = models.CharField(max_length=21, blank=True)
    price = models.FloatField(null=True, blank=True)
    currency_type = models.CharField(max_length=75, blank=True)
    payment_method = models.CharField(max_length=30, blank=True)
    transfers = models.CharField(max_length=30, blank=True)
    transfer_duration = models.CharField(max_length=30, blank=True, null=True)
    class Meta:
        db_table = u'fare_attributes'

class Frequencies(models.Model):
    trip_id = models.CharField(max_length=45, blank=True)
    start_time = models.CharField(max_length=60, blank=True)
    end_time = models.CharField(max_length=60, blank=True)
    headway_secs = models.IntegerField(null=True, blank=True)
    exact_times = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'frequencies'

class Mysat(models.Model):
    route_id = models.CharField(max_length=45, blank=True)
    service_id = models.CharField(max_length=45, blank=True)
    trip_id = models.CharField(max_length=45, blank=True)
    trip_short_name = models.CharField(max_length=150, blank=True)
    trip_headsign = models.CharField(max_length=450, blank=True)
    direction_id = models.IntegerField(null=True, blank=True)
    block_id = models.CharField(max_length=48, blank=True)
    shape_id = models.IntegerField(null=True, blank=True)
    trip_bikes_allowed = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'mysat'

class Routes(models.Model):
    agency_id = models.CharField(max_length=300, blank=True)
    route_id = models.CharField(primary_key=True,max_length=45, blank=True)
    route_short_name = models.CharField(max_length=105, blank=True)
    route_long_name = models.CharField(max_length=105, blank=True)
    route_desc = models.CharField(max_length=1500, blank=True)
    route_type = models.CharField(max_length=240, blank=True)
    route_url = models.CharField(max_length=300, blank=True)
    route_color = models.CharField(max_length=240, blank=True)
    route_text_color = models.CharField(max_length=240, blank=True)
    class Meta:
        db_table = u'routes'
    def __unicode__(self):
	return 	    "unicode" + str(self.route_long_name)+str(self.route_desc)
    def blah(self):
	return dir(self)

class Shapes(models.Model):
    shape_id = models.IntegerField(null=True, blank=True)
    shape_pt_lat = models.FloatField(null=True, blank=True)
    shape_pt_lon = models.FloatField(null=True, blank=True)
    shape_pt_sequence = models.IntegerField(null=True, blank=True)
    shape_dist_traveled = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'shapes'

class Trips(models.Model):
    route_id = models.CharField(max_length=45, blank=True)
    service_id = models.CharField(max_length=45, blank=True)
    trip_id = models.CharField(primary_key=True,max_length=45, blank=True)
    trip_short_name = models.CharField(max_length=150, blank=True)
    trip_headsign = models.CharField(max_length=450, blank=True)
    direction_id = models.IntegerField(null=True, blank=True)
    block_id = models.CharField(max_length=48, blank=True)
    shape_id = models.IntegerField(null=True, blank=True)
    trip_bikes_allowed = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'trips'

class StopTimes(models.Model):
    trips = models.ForeignKey(Trips) # causes foreign key failure
    trip_id = models.CharField(max_length=45, blank=True)
    arrival_time = models.TextField(blank=True) # This field type is a guess.
    departure_time = models.TextField(blank=True) # This field type is a guess.
    stop_id = models.CharField(max_length=24, blank=True)
    stop_sequence = models.IntegerField(null=True, blank=True)
    stop_headsign = models.CharField(max_length=90, blank=True)
    pickup_type = models.IntegerField(null=True, blank=True)
    drop_off_type = models.IntegerField(null=True, blank=True)
    shape_dist_traveled = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'stop_times'

class Stops(models.Model):
    stop_id = models.CharField(primary_key=True,max_length=24, blank=True)
    stop_code = models.CharField(max_length=24, blank=True)
    stop_name = models.CharField(max_length=240, blank=True)
    stop_desc = models.CharField(max_length=75, blank=True)
    stop_lat = models.FloatField(null=True, blank=True)
    stop_lon = models.FloatField(null=True, blank=True)
    zone_id = models.IntegerField(null=True, blank=True)
    stop_url = models.CharField(max_length=1500, blank=True)
    location_type = models.IntegerField(null=True, blank=True)
    parent_station = models.CharField(max_length=15, blank=True)
    stop_timezone = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'stops'

class Transfers(models.Model):
    from_stop_id = models.CharField(max_length=24, blank=True)
    to_stop_id = models.CharField(max_length=24, blank=True)
    transfer_type = models.IntegerField(null=True, blank=True)
    min_transfer_time = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'transfers'

