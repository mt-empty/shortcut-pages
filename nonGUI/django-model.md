# Django Model

> Source: https://docs.djangoproject.com/en/1.9/ref/models/fields/

> Aliases: django-model-field, django-models, django-models-field, django-models-fields, django-model-fields, django-orm

$ Field Types
    `AutoField                     {{An IntegerField that automatically increments according to available IDs}} 
    `BigIntegerField               {{A 64 bit integer, much like an IntegerField except that it is guaranteed to fit numbers from -9223372036854775808 to 9223372036854775807}} 
    `BinaryField                   {{A field to store raw binary data. It only supports bytes assignment}} 
    `BooleanField                  {{A true/false field}} 
    `CharField                     {{A string field, for small- to large-sized strings}} 
    `CommaSeparatedIntegerField    {{A field of integers separated by commas}} 
    `DateField                     {{A date, represented in Python by a datetime.date instance}} 
    `DateTimeField                 {{A date and time, represented in Python by a datetime.datetime instance}} 
    `DecimalField                  {{A fixed-precision decimal number, represented in Python by a Decimal instance}} 
    `DurationField                 {{A field for storing periods of time - modeled in Python by timedelta}} 
    `EmailField                    {{A CharField that checks that the value is a valid email address}} 
    `FileField                     {{A file-upload field}} 

$ Field Types Cont.
    `FloatField                    {{A floating-point number represented in Python by a float instance}} 
    `ImageField                    {{Inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image}} 
    `IntegerField                  {{An integer. Values from -2147483648 to 2147483647 are safe in all databases supported by Django}} 
    `GenericIPAddressField         {{An IPv4 or IPv6 address, in string format (e.g. 192.0.2.30 or 2a02:42fe::4)}} 
    `NullBooleanField              {{Like a BooleanField, but allows NULL as one of the options}} 
    `PositiveIntegerField          {{Like an IntegerField, but must be either positive or zero (0). Values from 0 to 2147483647 are safe in all databases supported by Django}} 
    `PositiveSmallIntegerField     {{Like a PositiveIntegerField, but only allows values under a certain (database-dependent) point. Values from 0 to 32767 are safe in all databases supported by Django}} 
    `SlugField                     {{A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs}} 
    `SmallIntegerField             {{Like an IntegerField, but only allows values under a certain (database-dependent) point. Values from -32768 to 32767 are safe in all databases supported by Django}} 
    `TextField                     {{A large text field. The default form widget for this field is a Textarea}} 
    `TimeField                     {{A time, represented in Python by a datetime.time instance. Accepts the same auto-population options as DateField}} 

$ Relationship Types
    `ForeignKey                    {{A many-to-one relationship. Requires a positional argument: the class to which the model is related}} 
    `ManyToManyField               {{A many-to-many relationship. Requires a positional argument: the class to which the model is related, which works exactly the same as it does for ForeignKey, including recursive and lazy relationships}} 
    `OneToOneField                 {{A one-to-one relationship. Conceptually, this is similar to a ForeignKey with unique=True, but the “reverse” side of the relation will directly return a single object}} 

