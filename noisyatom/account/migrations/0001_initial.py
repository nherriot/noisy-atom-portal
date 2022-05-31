# Generated by Django 2.2.27 on 2022-02-18 20:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='Enter the name you would like to give this address.', max_length=255, verbose_name='Name')),
                ('address_line1', models.CharField(blank=True, help_text='Enter your the address (line 1 of 4)', max_length=250, null=True, verbose_name='Address 1')),
                ('address_line2', models.CharField(blank=True, help_text='Enter your the address (line 2 of 4)', max_length=250, null=True, verbose_name='Address 2')),
                ('address_line3', models.CharField(blank=True, help_text='Enter your the address (line 3 of 4)', max_length=250, null=True, verbose_name='Address 3')),
                ('address_line4', models.CharField(blank=True, help_text='Enter your the address (line 4 of 4)', max_length=250, null=True, verbose_name='Address 4')),
                ('postal_code', models.CharField(blank=True, help_text='Enter your the Postal or Zip Code ', max_length=25, null=True, verbose_name='Postal code')),
                ('city', models.CharField(blank=True, help_text='Enter the name of the city you are based', max_length=250, null=True, verbose_name='City')),
                ('state', models.CharField(blank=True, help_text='Enter your  State / Province', max_length=250, null=True, verbose_name='State/Province')),
                ('country', models.CharField(blank=True, choices=[('', '- Choose One -'), ('AF', 'Afghanistan'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AS', 'American Samoa'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctica'), ('AG', 'Antigua and Barbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BO', 'Bolivia'), ('BA', 'Bosnia and Herzegovina'), ('BW', 'Botswana'), ('BV', 'Bouvet Island'), ('BR', 'Brazil'), ('IO', 'British Indian Ocean Territory'), ('BN', 'Brunei Darussalam'), ('BG', 'Bulgaria'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('KH', 'Cambodia'), ('CM', 'Cameroon'), ('CA', 'Canada'), ('CV', 'Cape Verde'), ('KY', 'Cayman Islands'), ('CF', 'Central African Republic'), ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CX', 'Christmas Island'), ('CC', 'Cocos (Keeling) Islands'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CG', 'Congo'), ('CD', 'Congo, The Democratic Republic'), ('CK', 'Cook Islands'), ('CR', 'Costa Rica'), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CY', 'Cyprus'), ('CZ', 'Czech Republic'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('TL', 'East Timor'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('ET', 'Ethiopia'), ('FK', 'Falkland Islands (Malvinas)'), ('FO', 'Faroe Islands'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GP', 'French Antilles Guadeloupe'), ('GF', 'French Guiana'), ('PF', 'French Polynesia'), ('TF', 'French Southern Territories'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GB', 'Great Britain (UK)'), ('GR', 'Greece'), ('GL', 'Greenland'), ('GD', 'Grenada'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('HM', 'Heard Island & McDonald Island'), ('HN', 'Honduras'), ('HK', 'Hong Kong'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IL', 'Israel'), ('IT', 'Italy'), ('CI', 'Ivory Coast'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', "Lao People's Democratic Rep."), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libya'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MO', 'Macau'), ('MK', 'Macedonia'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshall Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('YT', 'Mayotte'), ('MX', 'Mexico'), ('FM', 'Micronesia, Federated States'), ('MD', 'Moldova, Republic of'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('AN', 'Netherlands Antilles'), ('NC', 'New Caledonia'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NU', 'Niue'), ('NF', 'Norfolk Island'), ('KP', 'North Korea'), ('MP', 'Northern Mariana Islands'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestinian Territory, Occ.'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PN', 'Pitcairn'), ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('QA', 'Qatar'), ('RE', 'Reunion'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('GS', 'S. Georgia and S. Sandwich Isls.'), ('SH', 'Saint Helena'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('PM', 'Saint Pierre and Miquelon'), ('VC', 'Saint Vincent & the Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome and Principe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'), ('KR', 'South Korea'), ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SJ', 'Svalbard and Jan Mayen'), ('SZ', 'Swaziland'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syria'), ('TW', 'Taiwan'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania, United Republic of'), ('TH', 'Thailand'), ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TC', 'Turks and Caicos Islands'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('GB', 'United Kingdom'), ('US', 'United States'), ('UM', 'United States Minor Islands'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VA', 'Vatican City'), ('VE', 'Venezuela'), ('VG', 'Virgin Islands, British'), ('VI', 'Virgin Islands, U.S.'), ('VN', 'Viet Nam'), ('WF', 'Wallis and Futuna'), ('EH', 'Western Sahara'), ('YE', 'Yemen'), ('YU', 'Yugoslavia (former)'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], help_text='Enter your Country ', max_length=2, null=True, verbose_name='Country')),
                ('phone', models.CharField(blank=True, help_text='Enter the your phone number', max_length=250, null=True, verbose_name='Phone')),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
            ],
            options={
                'verbose_name_plural': 'Customer Addresses',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='Enter the name you would like to give this address.', max_length=255, verbose_name='Name')),
                ('description', models.TextField(blank=True, help_text='Please provide any extra description for this company.', null=True, verbose_name='Description')),
                ('vat', models.CharField(blank=True, help_text='VAT Registration', max_length=250, null=True, verbose_name='VAT Registration')),
                ('company_number', models.CharField(blank=True, help_text='Government allocated company number - e.g. HMRC Company Number', max_length=250, null=True, verbose_name='Company Number')),
                ('company_url', models.URLField(default='http://www.example.com', help_text='This is a unique URI to describe the callback used by the OAuth2 server', max_length=254, validators=[django.core.validators.URLValidator])),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('addresses', models.ManyToManyField(related_name='addresses_company_set', to='account.CustomerAddress')),
            ],
        ),
    ]
