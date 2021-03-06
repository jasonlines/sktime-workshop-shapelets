import numpy as np
from numpy import testing

from sktime.classifiers.proximity import ProximityForest, ProximityStump, ProximityTree
from sktime.datasets import load_gunpoint


def run_classifier_on_dataset(classifier, dataset_loader,
                              expected_predict_probas,
                              expected_predictions):
    X_train, y_train = dataset_loader(split = 'TRAIN', return_X_y = True)
    X_test, y_test = dataset_loader(split = 'TEST', return_X_y = True)
    classifier.fit(X_train, y_train)
    predict_probas = classifier.predict_proba(X_test)
    testing.assert_array_equal(predict_probas, expected_predict_probas)
    predictions = classifier.predict(X_test)
    testing.assert_array_equal(predictions, expected_predictions)


def test_proximity_forest_on_gunpoint():
    classifier = ProximityForest(debug = True, random_state = 0, num_trees = 10, num_stump_evaluations = 5)
    run_classifier_on_dataset(classifier, load_gunpoint, forest_gunpoint_predict_probas, forest_gunpoint_predictions)


def test_proximity_tree_on_gunpoint():
    classifier = ProximityTree(debug = True, random_state = 0, num_stump_evaluations = 5)
    run_classifier_on_dataset(classifier, load_gunpoint, tree_gunpoint_predict_probas, tree_gunpoint_predictions)


def test_proximity_stump_on_gunpoint():
    classifier = ProximityStump(debug = True, random_state = 0)
    run_classifier_on_dataset(classifier, load_gunpoint, stump_gunpoint_predict_probas, stump_gunpoint_predictions)


stump_gunpoint_predict_probas = np.array([
[0.10603768817209419,0.8939623118279059,],
[0.9561259718477505,0.04387402815224952,],
[0.3051248428859005,0.6948751571140995,],
[0.14592347448140314,0.8540765255185969,],
[0.9075214781964317,0.09247852180356826,],
[0.9597888808004567,0.04021111919954339,],
[0.10055315181278043,0.8994468481872195,],
[0.0625597076408307,0.9374402923591694,],
[0.682639755957531,0.31736024404246904,],
[0.9092771436885807,0.09072285631141935,],
[0.9108620847563125,0.08913791524368748,],
[0.10904115952810137,0.8909588404718985,],
[0.94248757228757,0.05751242771243007,],
[0.10620614838124125,0.8937938516187588,],
[0.135231522142502,0.864768477857498,],
[0.8765570827843974,0.12344291721560262,],
[0.9324222923016173,0.06757770769838259,],
[0.8360433834544294,0.16395661654557056,],
[0.8402025306254441,0.15979746937455586,],
[0.9188251490845515,0.08117485091544856,],
[0.2183372525971328,0.7816627474028671,],
[0.06448130940266253,0.9355186905973375,],
[0.893032512804443,0.10696748719555707,],
[0.917595958564862,0.08240404143513795,],
[0.20178317122968042,0.7982168287703195,],
[0.0832697492047478,0.9167302507952522,],
[0.10013396316200862,0.8998660368379914,],
[0.09998560520742716,0.9000143947925728,],
[0.7882404923178846,0.2117595076821153,],
[0.8421079778887711,0.15789202211122894,],
[0.9482954930456089,0.051704506954391105,],
[0.07704004551321497,0.922959954486785,],
[0.06983075087436902,0.9301692491256309,],
[0.9234865788205512,0.07651342117944887,],
[0.9331406268281015,0.0668593731718986,],
[0.7524175918167889,0.247582408183211,],
[0.8530912660313132,0.1469087339686868,],
[0.8342162404445508,0.16578375955544927,],
[0.24933426766760855,0.7506657323323914,],
[0.8244820485189502,0.17551795148104968,],
[0.9244891419150268,0.07551085808497307,],
[0.21112968615048397,0.788870313849516,],
[0.8419910987270829,0.15800890127291717,],
[0.876359696311348,0.12364030368865196,],
[0.1502869171013108,0.8497130828986893,],
[0.0835514790180062,0.9164485209819938,],
[0.10938323406446096,0.8906167659355391,],
[0.8018116723279473,0.19818832767205274,],
[0.9519229039679727,0.04807709603202724,],
[0.6953969310551044,0.3046030689448957,],
[0.7666464385565022,0.23335356144349784,],
[0.08273450121006991,0.9172654987899301,],
[0.8320197396589065,0.1679802603410935,],
[0.17060792528313296,0.829392074716867,],
[0.916642697921122,0.083357302078878,],
[0.08724156238157246,0.9127584376184275,],
[0.0636560273411289,0.9363439726588711,],
[0.9526050463219856,0.04739495367801427,],
[0.8314852676097299,0.1685147323902701,],
[0.9631265356036068,0.036873464396393184,],
[0.09115938653667788,0.9088406134633221,],
[0.29678866542420174,0.7032113345757982,],
[0.10541232088360242,0.8945876791163976,],
[0.7786694300584922,0.2213305699415078,],
[0.8474352993555013,0.1525647006444987,],
[0.8178327805484974,0.18216721945150258,],
[0.16719826545469393,0.8328017345453061,],
[0.9063698860063889,0.09363011399361104,],
[0.9444532287719893,0.05554677122801064,],
[0.9543465320917582,0.04565346790824174,],
[0.9184339992715822,0.08156600072841776,],
[0.926631572169125,0.07336842783087504,],
[0.8071556658567556,0.19284433414324434,],
[0.03861683559311905,0.961383164406881,],
[0.04729924138406089,0.9527007586159392,],
[0.9500677947748436,0.04993220522515649,],
[0.9392125000713661,0.06078749992863394,],
[0.22673951375311735,0.7732604862468826,],
[0.07200895822364223,0.9279910417763578,],
[0.915287624862642,0.08471237513735791,],
[0.08574487071882218,0.9142551292811778,],
[0.09135416159842172,0.9086458384015783,],
[0.24896053979938085,0.7510394602006192,],
[0.9425776250123775,0.05742237498762234,],
[0.9403408236524557,0.05965917634754426,],
[0.9566424469358602,0.04335755306413984,],
[0.08436953304020646,0.9156304669597934,],
[0.8489132937396222,0.15108670626037782,],
[0.9480867332322852,0.05191326676771478,],
[0.905431566154277,0.09456843384572303,],
[0.9606419130310404,0.039358086968959566,],
[0.054485081510973525,0.9455149184890266,],
[0.8423110696646189,0.15768893033538106,],
[0.07487155821157969,0.9251284417884204,],
[0.958761143208338,0.04123885679166191,],
[0.9531770084745074,0.0468229915254926,],
[0.9486351247316754,0.05136487526832453,],
[0.052946066971494996,0.947053933028505,],
[0.10500794085103622,0.8949920591489637,],
[0.8715117044903885,0.12848829550961147,],
[0.07016382059899738,0.9298361794010026,],
[0.1670549369265967,0.8329450630734033,],
[0.10593163546743134,0.8940683645325687,],
[0.7555458886663514,0.24445411133364847,],
[0.8451928460067745,0.15480715399322562,],
[0.8002583198264213,0.19974168017357866,],
[0.8951778351657933,0.10482216483420677,],
[0.24534023958177145,0.7546597604182286,],
[0.9500670884495496,0.049932911550450355,],
[0.9486580949270952,0.051341905072904814,],
[0.8992527814709672,0.10074721852903289,],
[0.93305553934421,0.06694446065578999,],
[0.09658524116679156,0.9034147588332084,],
[0.05697546581691373,0.9430245341830863,],
[0.8328133940266559,0.16718660597334414,],
[0.14871779795313048,0.8512822020468696,],
[0.06845856882987326,0.9315414311701268,],
[0.1487871475288874,0.8512128524711127,],
[0.9238996541701061,0.07610034582989386,],
[0.07349110508429829,0.9265088949157017,],
[0.16280508034185803,0.837194919658142,],
[0.10363107063988435,0.8963689293601157,],
[0.9481009872805324,0.05189901271946766,],
[0.25546734667773496,0.7445326533222649,],
[0.09284648453971389,0.9071535154602861,],
[0.13842327124464163,0.8615767287553584,],
[0.13944426637331603,0.860555733626684,],
[0.7858022980350545,0.2141977019649455,],
[0.05750263016563208,0.9424973698343679,],
[0.2572656429739673,0.7427343570260326,],
[0.056615366218990264,0.9433846337810097,],
[0.8858536549346397,0.1141463450653603,],
[0.15912008522239246,0.8408799147776075,],
[0.9448991357504882,0.055100864249511765,],
[0.11561221284594889,0.8843877871540511,],
[0.19642214540639039,0.8035778545936096,],
[0.09701805300619219,0.9029819469938077,],
[0.8474438248156801,0.15255617518431983,],
[0.1014850647171444,0.8985149352828555,],
[0.8047116095528037,0.19528839044719623,],
[0.17920763491989306,0.820792365080107,],
[0.139462819391685,0.860537180608315,],
[0.9336881229253923,0.06631187707460764,],
[0.2877878921440371,0.712212107855963,],
[0.9243043024896173,0.07569569751038269,],
[0.9576130450419078,0.04238695495809217,],
[0.8477411563159867,0.15225884368401343,],
[0.891202766655638,0.10879723334436198,],
[0.1081041381211183,0.8918958618788817,],
[0.09128199320696224,0.9087180067930377,],
])
stump_gunpoint_predictions = np.array(['2','1','2','2','1','1','2','2','1','1','1','2','1','2','2','1','1','1'
,'1','1','2','2','1','1','2','2','2','2','1','1','1','2','2','1','1','1'
,'1','1','2','1','1','2','1','1','2','2','2','1','1','1','1','2','1','2'
,'1','2','2','1','1','1','2','2','2','1','1','1','2','1','1','1','1','1'
,'1','2','2','1','1','2','2','1','2','2','2','1','1','1','2','1','1','1'
,'1','2','1','2','1','1','1','2','2','1','2','2','2','1','1','1','1','2'
,'1','1','1','1','2','2','1','2','2','2','1','2','2','2','1','2','2','2'
,'2','1','2','2','2','1','2','1','2','2','2','1','2','1','2','2','1','2'
,'1','1','1','1','2','2'])
tree_gunpoint_predict_probas = np.array([
[1,0,],
[0,1,],
[0,1,],
[1,0,],
[1,0,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[1,0,],
[0,1,],
[1,0,],
[1,0,],
[0,1,],
[1,0,],
[0,1,],
[0,1,],
[0,1,],
[1,0,],
[0,1,],
[1,0,],
[1,0,],
[1,0,],
[1,0,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[1,0,],
[0,1,],
[0,1,],
[1,0,],
[0,1,],
[1,0,],
[1,0,],
[1,0,],
[1,0,],
[0,1,],
[0,1,],
[1,0,],
[0,1,],
[0,1,],
[0,1,],
[1,0,],
[0,1,],
[1,0,],
[1,0,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[1,0,],
[0,1,],
[1,0,],
[0,1,],
[0,1,],
[1,0,],
[0,1,],
[1,0,],
[1,0,],
[0,1,],
[0,1,],
[0,1,],
[1,0,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[1,0,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[1,0,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[1,0,],
[0,1,],
[0,1,],
[1,0,],
[0,1,],
[0,1,],
[1,0,],
[1,0,],
[0,1,],
[0,1,],
[0,1,],
[1,0,],
[0,1,],
[1,0,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[1,0,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[1,0,],
[0,1,],
[0,1,],
[1,0,],
[1,0,],
[0,1,],
[1,0,],
[0,1,],
[0,1,],
[1,0,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[1,0,],
[0,1,],
[1,0,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[0,1,],
[1,0,],
])
tree_gunpoint_predictions = np.array(['1', '2', '2', '1', '2', '2', '1', '2', '2', '1', '2', '1', '1', '1', '1', '2',
                                       '2', '2'
                                              , '2', '2', '1', '1', '2', '2', '2', '1', '2', '1', '2', '2', '1', '2',
                                       '2', '2', '2', '1'
                                              , '2', '1', '1', '2', '2', '1', '1', '2', '2', '1', '1', '2', '1', '2',
                                       '1', '1', '1', '2'
                                              , '1', '1', '1', '2', '1', '1', '1', '1', '2', '1', '2', '2', '2', '2',
                                       '2', '2', '2', '2'
                                              , '2', '2', '2', '2', '2', '2', '2', '1', '2', '2', '2', '2', '2', '2',
                                       '2', '2', '1', '1'
                                              , '2', '2', '2', '2', '2', '1', '2', '2', '2', '1', '2', '1', '2', '2',
                                       '2', '1', '1', '2'
                                              , '1', '1', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '1', '2',
                                       '2', '1', '1', '2'
                                              , '1', '2', '2', '1', '2', '2', '1', '2', '2', '2', '1', '2', '2', '2',
                                       '1', '2', '2', '2'
                                              , '1', '2', '1', '2', '2', '1'])
forest_gunpoint_predict_probas = np.array([
[0.9,0.1,],
[0.2,0.8,],
[0.0,1.0,],
[0.9,0.1,],
[1.0,0.0,],
[0.2,0.8,],
[0.9,0.1,],
[0.1,0.9,],
[0.1,0.9,],
[0.9,0.1,],
[0.5,0.5,],
[0.8,0.2,],
[0.3,0.7,],
[0.8,0.2,],
[0.8,0.2,],
[0.6,0.4,],
[0.7,0.3,],
[0.3,0.7,],
[0.2,0.8,],
[0.1,0.9,],
[0.9,0.1,],
[0.2,0.8,],
[1.0,0.0,],
[1.0,0.0,],
[1.0,0.0,],
[0.3,0.7,],
[0.8,0.2,],
[0.8,0.2,],
[0.3,0.7,],
[0.8,0.2,],
[0.7,0.3,],
[0.1,0.9,],
[0.2,0.8,],
[0.8,0.2,],
[0.7,0.3,],
[0.9,0.1,],
[0.9,0.1,],
[0.6,0.4,],
[0.9,0.1,],
[0.4,0.6,],
[0.9,0.1,],
[0.1,0.9,],
[0.7,0.3,],
[0.7,0.3,],
[0.1,0.9,],
[0.8,0.2,],
[0.2,0.8,],
[0.4,0.6,],
[0.6,0.4,],
[0.1,0.9,],
[0.2,0.8,],
[0.1,0.9,],
[0.8,0.2,],
[0.2,0.8,],
[0.9,0.1,],
[1.0,0.0,],
[0.2,0.8,],
[0.1,0.9,],
[0.9,0.1,],
[0.3,0.7,],
[0.8,0.2,],
[0.2,0.8,],
[0.8,0.2,],
[0.4,0.6,],
[0.0,1.0,],
[0.7,0.3,],
[0.9,0.1,],
[0.1,0.9,],
[0.1,0.9,],
[0.2,0.8,],
[0.0,1.0,],
[0.1,0.9,],
[0.3,0.7,],
[0.2,0.8,],
[0.2,0.8,],
[0.1,0.9,],
[0.1,0.9,],
[0.0,1.0,],
[0.1,0.9,],
[0.9,0.1,],
[0.9,0.1,],
[0.9,0.1,],
[0.0,1.0,],
[0.0,1.0,],
[0.1,0.9,],
[0.0,1.0,],
[0.9,0.1,],
[0.3,0.7,],
[0.8,0.2,],
[0.6,0.4,],
[0.7,0.3,],
[0.2,0.8,],
[0.8,0.2,],
[0.2,0.8,],
[0.4,0.6,],
[0.8,0.2,],
[0.1,0.9,],
[0.1,0.9,],
[0.9,0.1,],
[0.7,0.3,],
[0.1,0.9,],
[1.0,0.0,],
[1.0,0.0,],
[0.2,0.8,],
[0.2,0.8,],
[0.8,0.2,],
[0.8,0.2,],
[0.2,0.8,],
[0.7,0.3,],
[0.2,0.8,],
[0.1,0.9,],
[0.1,0.9,],
[0.7,0.3,],
[0.2,0.8,],
[0.9,0.1,],
[0.8,0.2,],
[0.2,0.8,],
[1.0,0.0,],
[0.8,0.2,],
[0.1,0.9,],
[0.9,0.1,],
[0.2,0.8,],
[0.1,0.9,],
[0.1,0.9,],
[0.9,0.1,],
[0.1,0.9,],
[0.9,0.1,],
[0.6,0.4,],
[0.1,0.9,],
[0.1,0.9,],
[0.1,0.9,],
[0.1,0.9,],
[0.9,0.1,],
[0.5,0.5,],
[0.7,0.3,],
[0.0,1.0,],
[0.8,0.2,],
[0.1,0.9,],
[0.8,0.2,],
[0.7,0.3,],
[0.2,0.8,],
[0.4,0.6,],
[0.8,0.2,],
[0.0,1.0,],
[0.8,0.2,],
[0.2,0.8,],
[0.6,0.4,],
[0.2,0.8,],
[0.0,1.0,],
[0.7,0.3,],
])
forest_gunpoint_predictions = np.array(['1','2','2','1','1','2','1','2','2','1','2','1',
                                                                     '2','1','1','1','1','2'
,'2','2','1','2','1','1','1','2','1','1','2','1','1','2','2','1','1','1'
,'1','1','1','2','1','2','2','1','2','1','2','2','1','2','2','2','1','2'
,'1','1','2','2','1','2','1','2','1','2','2','1','1','2','2','2','2','2'
,'2','2','2','2','2','2','2','1','1','1','2','2','2','2','1','2','1','1'
,'1','2','1','2','2','1','2','2','1','1','2','1','1','2','2','1','1','2'
,'1','2','2','2','1','2','1','1','2','1','1','2','1','2','2','2','1','2'
,'1','1','2','2','2','2','1','1','1','2','1','2','1','1','2','1','1','2'
,'1','2','1','2','2','1'])

# code to generate predictions below:
# import sktime.datasets
# import numpy as np
# import sktime.classifiers.proximity
#
# def print_array(array):
#     print('[')
#     for sub_array in array:
#         print('[', end='')
#         for value in sub_array:
#             print(value.astype(str), end='')
#             print(',', end='')
#         print('],')
#     print(']')
#
# if __name__ == "__main__":
##    change below to prox stump / tree / forest as required
#     classifier = sktime.classifiers.proximity.ProximityForest(debug = True, random_state = 0,
#                                                               num_trees = 10, # not needed for prox tree / stump
#                                                               num_stump_evaluations = 5 # not needed for prox stump
#                                                               )
#     X_train, y_train = sktime.datasets.load_gunpoint(split = 'TRAIN', return_X_y = True)
#     X_test, y_test = sktime.datasets.load_gunpoint(split = 'TEST', return_X_y = True)
#     classifier.fit(X_train, y_train)
#     predict_probas = classifier.predict_proba(X_test)
#     print_array(predict_probas)
#     predictions = classifier.predict(X_test)
#     print(predictions)
