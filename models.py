from django.db import models

# Create your models here.


class Hall (models.Model):

    name = models.CharField(
        verbose_name='название зала',
        max_length=50
    )
    sits = models.IntegerField(
        verbose_name='количество мест',
        default=30
    )

    booked_sits = models.IntegerField(
        verbose_name='забронировано',
        default=0
    )

    created = models.DateTimeField(
        verbose_name='created',
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='updated',
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self):
        return f'Hall №{self.pk}, name: {self.name}, sits: {self.sits}, booked: {self.booked_sits}, update: {self.updated}'



# имеющиеся залы:

# Hall №4, name: Hall1, sits: 80, booked: 0, update: 2021-03-19 10:23:29.961161+00:00
# Hall №5, name: Hall2, sits: 67, booked: 0, update: 2021-03-19 10:23:30.212667+00:00
# Hall №6, name: Hall3, sits: 96, booked: 0, update: 2021-03-19 10:23:30.266659+00:00
# Hall №7, name: Hall4, sits: 60, booked: 0, update: 2021-03-19 10:23:30.313152+00:00
# Hall №8, name: Hall5, sits: 43, booked: 0, update: 2021-03-19 10:23:30.358981+00:00
# Hall №9, name: Hall6, sits: 47, booked: 0, update: 2021-03-19 10:23:30.406603+00:00
# Hall №10, name: Hall7, sits: 99, booked: 0, update: 2021-03-19 10:23:30.450450+00:00
# Hall №11, name: Hall8, sits: 80, booked: 0, update: 2021-03-19 10:23:30.497234+00:00
# Hall №12, name: Hall9, sits: 47, booked: 0, update: 2021-03-19 10:23:30.542724+00:00
# Hall №13, name: Hall10, sits: 45, booked: 0, update: 2021-03-19 10:23:30.652649+00:00
# Hall №14, name: Hall11, sits: 86, booked: 0, update: 2021-03-19 10:23:30.699272+00:00
# Hall №15, name: Hall12, sits: 86, booked: 0, update: 2021-03-19 10:23:30.737733+00:00
# Hall №16, name: Hall13, sits: 60, booked: 0, update: 2021-03-19 10:23:30.782083+00:00
# Hall №17, name: Hall14, sits: 42, booked: 0, update: 2021-03-19 10:23:30.827425+00:00
# Hall №18, name: Hall15, sits: 38, booked: 0, update: 2021-03-19 10:23:30.873862+00:00
# Hall №19, name: Hall16, sits: 86, booked: 0, update: 2021-03-19 10:23:30.918477+00:00
# Hall №20, name: Hall17, sits: 96, booked: 0, update: 2021-03-19 10:23:30.957144+00:00
# Hall №21, name: Hall18, sits: 97, booked: 0, update: 2021-03-19 10:23:31.003750+00:00
# Hall №22, name: Hall19, sits: 62, booked: 0, update: 2021-03-19 10:23:31.049479+00:00
# Hall №23, name: Hall20, sits: 70, booked: 0, update: 2021-03-19 10:23:31.088147+00:00
# Hall №24, name: Hall21, sits: 59, booked: 0, update: 2021-03-19 10:23:31.133157+00:00
# Hall №25, name: Hall22, sits: 47, booked: 0, update: 2021-03-19 10:23:31.179422+00:00
# Hall №26, name: Hall23, sits: 48, booked: 0, update: 2021-03-19 10:23:31.226800+00:00
# Hall №27, name: Hall24, sits: 87, booked: 0, update: 2021-03-19 10:23:31.272056+00:00
# Hall №28, name: Hall25, sits: 59, booked: 0, update: 2021-03-19 10:23:31.311522+00:00
# Hall №29, name: Hall26, sits: 74, booked: 0, update: 2021-03-19 10:23:31.356256+00:00
# Hall №30, name: Hall27, sits: 37, booked: 0, update: 2021-03-19 10:23:31.402014+00:00
# Hall №31, name: Hall28, sits: 64, booked: 0, update: 2021-03-19 10:23:31.448183+00:00
# Hall №32, name: Hall29, sits: 50, booked: 0, update: 2021-03-19 10:23:31.493953+00:00
# Hall №33, name: Hall30, sits: 89, booked: 0, update: 2021-03-19 10:23:31.533710+00:00
# Hall №34, name: Hall31, sits: 61, booked: 0, update: 2021-03-19 10:23:31.579781+00:00
# Hall №35, name: Hall32, sits: 70, booked: 0, update: 2021-03-19 10:23:31.625405+00:00
# Hall №36, name: Hall33, sits: 66, booked: 0, update: 2021-03-19 10:23:31.672034+00:00
# Hall №37, name: Hall34, sits: 69, booked: 0, update: 2021-03-19 10:23:31.722203+00:00
# Hall №38, name: Hall35, sits: 41, booked: 0, update: 2021-03-19 10:23:31.766667+00:00
# Hall №39, name: Hall36, sits: 86, booked: 0, update: 2021-03-19 10:23:31.806265+00:00
# Hall №40, name: Hall37, sits: 45, booked: 0, update: 2021-03-19 10:23:31.850908+00:00
# Hall №41, name: Hall38, sits: 54, booked: 0, update: 2021-03-19 10:23:31.890374+00:00
# Hall №42, name: Hall39, sits: 58, booked: 0, update: 2021-03-19 10:23:31.934290+00:00
# Hall №43, name: Hall40, sits: 65, booked: 0, update: 2021-03-19 10:23:31.973052+00:00
# Hall №44, name: Hall41, sits: 69, booked: 0, update: 2021-03-19 10:23:32.018980+00:00
# Hall №45, name: Hall42, sits: 59, booked: 0, update: 2021-03-19 10:23:32.070130+00:00
# Hall №46, name: Hall43, sits: 33, booked: 0, update: 2021-03-19 10:23:32.116166+00:00
# Hall №47, name: Hall44, sits: 41, booked: 0, update: 2021-03-19 10:23:32.378536+00:00
# Hall №48, name: Hall45, sits: 49, booked: 0, update: 2021-03-19 10:23:33.002100+00:00
# Hall №49, name: Hall46, sits: 97, booked: 0, update: 2021-03-19 10:23:33.121620+00:00
# Hall №50, name: Hall47, sits: 67, booked: 0, update: 2021-03-19 10:23:33.241751+00:00
# Hall №51, name: Hall48, sits: 41, booked: 0, update: 2021-03-19 10:23:33.369616+00:00
# Hall №52, name: Hall49, sits: 71, booked: 0, update: 2021-03-19 10:23:33.481109+00:00
# Hall №53, name: Hall50, sits: 75, booked: 0, update: 2021-03-19 10:23:33.608324+00:00
# Hall №54, name: Hall51, sits: 47, booked: 0, update: 2021-03-19 10:23:33.712984+00:00
# Hall №55, name: Hall52, sits: 83, booked: 0, update: 2021-03-19 10:23:33.792990+00:00
# Hall №56, name: Hall53, sits: 63, booked: 0, update: 2021-03-19 10:23:33.886632+00:00
# Hall №57, name: Hall54, sits: 32, booked: 0, update: 2021-03-19 10:23:33.990080+00:00
# Hall №58, name: Hall55, sits: 61, booked: 0, update: 2021-03-19 10:23:34.035531+00:00
# Hall №59, name: Hall56, sits: 67, booked: 0, update: 2021-03-19 10:23:34.083066+00:00
# Hall №60, name: Hall57, sits: 78, booked: 0, update: 2021-03-19 10:23:34.127154+00:00
# Hall №61, name: Hall58, sits: 100, booked: 0, update: 2021-03-19 10:23:34.186930+00:00
# Hall №62, name: Hall59, sits: 37, booked: 0, update: 2021-03-19 10:23:34.233158+00:00
# Hall №63, name: Hall60, sits: 39, booked: 0, update: 2021-03-19 10:23:34.279072+00:00
# Hall №64, name: Hall61, sits: 39, booked: 0, update: 2021-03-19 10:23:34.325344+00:00
# Hall №65, name: Hall62, sits: 44, booked: 0, update: 2021-03-19 10:23:34.371731+00:00
# Hall №66, name: Hall63, sits: 58, booked: 0, update: 2021-03-19 10:23:34.417560+00:00
# Hall №67, name: Hall64, sits: 44, booked: 0, update: 2021-03-19 10:23:34.463643+00:00
# Hall №68, name: Hall65, sits: 89, booked: 0, update: 2021-03-19 10:23:34.569561+00:00
# Hall №69, name: Hall66, sits: 53, booked: 0, update: 2021-03-19 10:23:34.614017+00:00
# Hall №70, name: Hall67, sits: 98, booked: 0, update: 2021-03-19 10:23:34.677882+00:00
# Hall №71, name: Hall68, sits: 83, booked: 0, update: 2021-03-19 10:23:34.724816+00:00
# Hall №72, name: Hall69, sits: 42, booked: 0, update: 2021-03-19 10:23:34.769609+00:00
# Hall №73, name: Hall70, sits: 46, booked: 0, update: 2021-03-19 10:23:34.815915+00:00
# Hall №74, name: Hall71, sits: 33, booked: 0, update: 2021-03-19 10:23:34.862155+00:00
# Hall №75, name: Hall72, sits: 86, booked: 0, update: 2021-03-19 10:23:34.908875+00:00
# Hall №76, name: Hall73, sits: 70, booked: 0, update: 2021-03-19 10:23:34.968071+00:00
# Hall №77, name: Hall74, sits: 100, booked: 0, update: 2021-03-19 10:23:35.013750+00:00
# Hall №78, name: Hall75, sits: 40, booked: 0, update: 2021-03-19 10:23:35.060519+00:00
# Hall №79, name: Hall76, sits: 32, booked: 0, update: 2021-03-19 10:23:35.122345+00:00
# Hall №80, name: Hall77, sits: 35, booked: 0, update: 2021-03-19 10:23:35.176239+00:00
# Hall №81, name: Hall78, sits: 78, booked: 0, update: 2021-03-19 10:23:35.222945+00:00
# Hall №82, name: Hall79, sits: 97, booked: 0, update: 2021-03-19 10:23:35.310037+00:00
# Hall №83, name: Hall80, sits: 68, booked: 0, update: 2021-03-19 10:23:35.355590+00:00
# Hall №84, name: Hall81, sits: 81, booked: 0, update: 2021-03-19 10:23:35.406379+00:00
# Hall №85, name: Hall82, sits: 91, booked: 0, update: 2021-03-19 10:23:35.452233+00:00
# Hall №86, name: Hall83, sits: 52, booked: 0, update: 2021-03-19 10:23:35.497208+00:00
# Hall №87, name: Hall84, sits: 92, booked: 0, update: 2021-03-19 10:23:35.545592+00:00
# Hall №88, name: Hall85, sits: 61, booked: 0, update: 2021-03-19 10:23:35.591309+00:00
# Hall №89, name: Hall86, sits: 89, booked: 0, update: 2021-03-19 10:23:35.831967+00:00
# Hall №90, name: Hall87, sits: 53, booked: 0, update: 2021-03-19 10:23:36.345598+00:00
# Hall №91, name: Hall88, sits: 30, booked: 0, update: 2021-03-19 10:23:36.400083+00:00
# Hall №92, name: Hall89, sits: 56, booked: 0, update: 2021-03-19 10:23:36.463741+00:00
# Hall №93, name: Hall90, sits: 39, booked: 0, update: 2021-03-19 10:23:36.518539+00:00
# Hall №94, name: Hall91, sits: 88, booked: 0, update: 2021-03-19 10:23:36.589994+00:00
# Hall №95, name: Hall92, sits: 71, booked: 0, update: 2021-03-19 10:23:36.643398+00:00
# Hall №96, name: Hall93, sits: 47, booked: 0, update: 2021-03-19 10:23:36.700229+00:00
# Hall №97, name: Hall94, sits: 62, booked: 0, update: 2021-03-19 10:23:36.760731+00:00
# Hall №98, name: Hall95, sits: 44, booked: 0, update: 2021-03-19 10:23:36.815126+00:00
# Hall №99, name: Hall96, sits: 78, booked: 0, update: 2021-03-19 10:23:36.869658+00:00
# Hall №100, name: Hall97, sits: 42, booked: 0, update: 2021-03-19 10:23:36.924795+00:00
# Hall №101, name: Hall98, sits: 84, booked: 0, update: 2021-03-19 10:23:36.979637+00:00
# Hall №102, name: Hall99, sits: 39, booked: 0, update: 2021-03-19 10:23:37.034969+00:00
# Hall №103, name: Hall100, sits: 93, booked: 0, update: 2021-03-19 10:23:37.089936+00:00
# Hall №104, name: Hall101, sits: 36, booked: 0, update: 2021-03-19 10:23:37.152949+00:00
# Hall №105, name: Hall102, sits: 59, booked: 0, update: 2021-03-19 10:23:37.213089+00:00
# Hall №106, name: Hall103, sits: 74, booked: 0, update: 2021-03-19 10:23:37.267072+00:00
# Hall №107, name: Hall104, sits: 36, booked: 0, update: 2021-03-19 10:23:37.320255+00:00
# Hall №108, name: Hall105, sits: 36, booked: 0, update: 2021-03-19 10:23:37.375110+00:00
# Hall №109, name: Hall106, sits: 38, booked: 0, update: 2021-03-19 10:23:37.429935+00:00
# Hall №110, name: Hall107, sits: 59, booked: 0, update: 2021-03-19 10:23:37.485222+00:00
# Hall №111, name: Hall108, sits: 74, booked: 0, update: 2021-03-19 10:23:37.539890+00:00
# Hall №112, name: Hall109, sits: 75, booked: 0, update: 2021-03-19 10:23:37.603286+00:00
# Hall №113, name: Hall110, sits: 84, booked: 0, update: 2021-03-19 10:23:37.662025+00:00
# Hall №114, name: Hall111, sits: 86, booked: 0, update: 2021-03-19 10:23:37.716762+00:00
# Hall №115, name: Hall112, sits: 93, booked: 0, update: 2021-03-19 10:23:37.789754+00:00
# Hall №116, name: Hall113, sits: 96, booked: 0, update: 2021-03-19 10:23:38.452209+00:00
# Hall №117, name: Hall114, sits: 45, booked: 0, update: 2021-03-19 10:23:38.533616+00:00
# Hall №118, name: Hall115, sits: 39, booked: 0, update: 2021-03-19 10:23:38.587433+00:00
# Hall №119, name: Hall116, sits: 77, booked: 0, update: 2021-03-19 10:23:38.643225+00:00
# Hall №120, name: Hall117, sits: 91, booked: 0, update: 2021-03-19 10:23:38.697924+00:00
# Hall №121, name: Hall118, sits: 59, booked: 0, update: 2021-03-19 10:23:38.758179+00:00
# Hall №122, name: Hall119, sits: 82, booked: 0, update: 2021-03-19 10:23:38.812548+00:00
# Hall №123, name: Hall120, sits: 82, booked: 0, update: 2021-03-19 10:23:38.867518+00:00
# Hall №124, name: Hall121, sits: 50, booked: 0, update: 2021-03-19 10:23:38.922219+00:00
# Hall №125, name: Hall122, sits: 62, booked: 0, update: 2021-03-19 10:23:38.977255+00:00
# Hall №126, name: Hall123, sits: 63, booked: 0, update: 2021-03-19 10:23:39.032632+00:00
# Hall №127, name: Hall124, sits: 36, booked: 0, update: 2021-03-19 10:23:39.088052+00:00
# Hall №128, name: Hall125, sits: 84, booked: 0, update: 2021-03-19 10:23:39.146938+00:00
# Hall №129, name: Hall126, sits: 90, booked: 0, update: 2021-03-19 10:23:39.202255+00:00
# Hall №130, name: Hall127, sits: 41, booked: 0, update: 2021-03-19 10:23:39.257391+00:00
# Hall №131, name: Hall128, sits: 88, booked: 0, update: 2021-03-19 10:23:39.312687+00:00
# Hall №132, name: Hall129, sits: 37, booked: 0, update: 2021-03-19 10:23:39.383235+00:00
# Hall №133, name: Hall130, sits: 72, booked: 0, update: 2021-03-19 10:23:39.438442+00:00
# Hall №134, name: Hall131, sits: 95, booked: 0, update: 2021-03-19 10:23:39.494752+00:00
# Hall №135, name: Hall132, sits: 36, booked: 0, update: 2021-03-19 10:23:39.547815+00:00
# Hall №136, name: Hall133, sits: 88, booked: 0, update: 2021-03-19 10:23:39.611245+00:00
# Hall №137, name: Hall134, sits: 69, booked: 0, update: 2021-03-19 10:23:39.666293+00:00
# Hall №138, name: Hall135, sits: 76, booked: 0, update: 2021-03-19 10:23:39.744129+00:00
# Hall №139, name: Hall136, sits: 71, booked: 0, update: 2021-03-19 10:23:39.799879+00:00
# Hall №140, name: Hall137, sits: 60, booked: 0, update: 2021-03-19 10:23:39.854496+00:00
# Hall №141, name: Hall138, sits: 52, booked: 0, update: 2021-03-19 10:23:40.094587+00:00
# Hall №142, name: Hall139, sits: 65, booked: 0, update: 2021-03-19 10:23:40.619736+00:00
# Hall №143, name: Hall140, sits: 67, booked: 0, update: 2021-03-19 10:23:40.669726+00:00
# Hall №144, name: Hall141, sits: 36, booked: 0, update: 2021-03-19 10:23:40.715779+00:00
# Hall №145, name: Hall142, sits: 48, booked: 0, update: 2021-03-19 10:23:40.795900+00:00
# Hall №146, name: Hall143, sits: 61, booked: 0, update: 2021-03-19 10:23:40.851725+00:00
# Hall №147, name: Hall144, sits: 94, booked: 0, update: 2021-03-19 10:23:40.906639+00:00
# Hall №148, name: Hall145, sits: 46, booked: 0, update: 2021-03-19 10:23:40.962397+00:00
# Hall №149, name: Hall146, sits: 36, booked: 0, update: 2021-03-19 10:23:41.017632+00:00
# Hall №150, name: Hall147, sits: 41, booked: 0, update: 2021-03-19 10:23:41.072253+00:00
# Hall №151, name: Hall148, sits: 45, booked: 0, update: 2021-03-19 10:23:41.136010+00:00
# Hall №152, name: Hall149, sits: 100, booked: 0, update: 2021-03-19 10:23:41.191850+00:00
# Hall №153, name: Hall150, sits: 35, booked: 0, update: 2021-03-19 10:23:41.246175+00:00
# Hall №154, name: Hall151, sits: 89, booked: 0, update: 2021-03-19 10:23:41.301171+00:00
# Hall №155, name: Hall152, sits: 100, booked: 0, update: 2021-03-19 10:23:41.372046+00:00
# Hall №156, name: Hall153, sits: 89, booked: 0, update: 2021-03-19 10:23:41.442964+00:00
# Hall №157, name: Hall154, sits: 31, booked: 0, update: 2021-03-19 10:23:41.515263+00:00
# Hall №158, name: Hall155, sits: 38, booked: 0, update: 2021-03-19 10:23:41.570098+00:00
# Hall №159, name: Hall156, sits: 71, booked: 0, update: 2021-03-19 10:23:41.632942+00:00
# Hall №160, name: Hall157, sits: 37, booked: 0, update: 2021-03-19 10:23:41.688658+00:00
# Hall №161, name: Hall158, sits: 96, booked: 0, update: 2021-03-19 10:23:41.744337+00:00
# Hall №162, name: Hall159, sits: 66, booked: 0, update: 2021-03-19 10:23:41.799557+00:00
# Hall №163, name: Hall160, sits: 73, booked: 0, update: 2021-03-19 10:23:41.854624+00:00
# Hall №164, name: Hall161, sits: 38, booked: 0, update: 2021-03-19 10:23:41.900544+00:00
# Hall №165, name: Hall162, sits: 39, booked: 0, update: 2021-03-19 10:23:41.945727+00:00
# Hall №166, name: Hall163, sits: 49, booked: 0, update: 2021-03-19 10:23:42.001315+00:00
# Hall №167, name: Hall164, sits: 40, booked: 0, update: 2021-03-19 10:23:42.064452+00:00
# Hall №168, name: Hall165, sits: 51, booked: 0, update: 2021-03-19 10:23:42.268693+00:00
# Hall №169, name: Hall166, sits: 43, booked: 0, update: 2021-03-19 10:23:42.826210+00:00
# Hall №170, name: Hall167, sits: 93, booked: 0, update: 2021-03-19 10:23:42.871987+00:00
# Hall №171, name: Hall168, sits: 68, booked: 0, update: 2021-03-19 10:23:42.917952+00:00
# Hall №172, name: Hall169, sits: 100, booked: 0, update: 2021-03-19 10:23:42.972508+00:00
# Hall №173, name: Hall170, sits: 88, booked: 0, update: 2021-03-19 10:23:43.018490+00:00
# Hall №174, name: Hall171, sits: 87, booked: 0, update: 2021-03-19 10:23:43.073453+00:00
# Hall №175, name: Hall172, sits: 84, booked: 0, update: 2021-03-19 10:23:43.136145+00:00
# Hall №176, name: Hall173, sits: 96, booked: 0, update: 2021-03-19 10:23:43.182341+00:00
# Hall №177, name: Hall174, sits: 99, booked: 0, update: 2021-03-19 10:23:43.227521+00:00
# Hall №178, name: Hall175, sits: 73, booked: 0, update: 2021-03-19 10:23:43.274351+00:00
# Hall №179, name: Hall176, sits: 62, booked: 0, update: 2021-03-19 10:23:43.319805+00:00
# Hall №180, name: Hall177, sits: 44, booked: 0, update: 2021-03-19 10:23:43.366661+00:00
# Hall №181, name: Hall178, sits: 33, booked: 0, update: 2021-03-19 10:23:43.412969+00:00
# Hall №182, name: Hall179, sits: 38, booked: 0, update: 2021-03-19 10:23:43.499665+00:00
# Hall №183, name: Hall180, sits: 43, booked: 0, update: 2021-03-19 10:23:43.554879+00:00
# Hall №184, name: Hall181, sits: 90, booked: 0, update: 2021-03-19 10:23:43.600478+00:00
# Hall №185, name: Hall182, sits: 45, booked: 0, update: 2021-03-19 10:23:43.647142+00:00
# Hall №186, name: Hall183, sits: 78, booked: 0, update: 2021-03-19 10:23:43.694221+00:00
# Hall №187, name: Hall184, sits: 68, booked: 0, update: 2021-03-19 10:23:43.755234+00:00
# Hall №188, name: Hall185, sits: 83, booked: 0, update: 2021-03-19 10:23:43.801302+00:00
# Hall №189, name: Hall186, sits: 82, booked: 0, update: 2021-03-19 10:23:43.857462+00:00
# Hall №190, name: Hall187, sits: 37, booked: 0, update: 2021-03-19 10:23:43.902075+00:00
# Hall №191, name: Hall188, sits: 73, booked: 0, update: 2021-03-19 10:23:43.949260+00:00
# Hall №192, name: Hall189, sits: 88, booked: 0, update: 2021-03-19 10:23:43.995987+00:00
# Hall №193, name: Hall190, sits: 63, booked: 0, update: 2021-03-19 10:23:44.041545+00:00
# Hall №194, name: Hall191, sits: 63, booked: 0, update: 2021-03-19 10:23:44.087076+00:00
# Hall №195, name: Hall192, sits: 53, booked: 0, update: 2021-03-19 10:23:44.133520+00:00
# Hall №196, name: Hall193, sits: 68, booked: 0, update: 2021-03-19 10:23:44.179445+00:00
# Hall №197, name: Hall194, sits: 35, booked: 0, update: 2021-03-19 10:23:44.233971+00:00
# Hall №198, name: Hall195, sits: 79, booked: 0, update: 2021-03-19 10:23:44.279277+00:00
# Hall №199, name: Hall196, sits: 44, booked: 0, update: 2021-03-19 10:23:44.327384+00:00
# Hall №200, name: Hall197, sits: 34, booked: 0, update: 2021-03-19 10:23:44.371490+00:00
# Hall №201, name: Hall198, sits: 65, booked: 0, update: 2021-03-19 10:23:44.419061+00:00
# Hall №202, name: Hall199, sits: 86, booked: 0, update: 2021-03-19 10:23:44.465976+00:00
# Hall №203, name: Hall200, sits: 82, booked: 0, update: 2021-03-19 10:23:44.512860+00:00
