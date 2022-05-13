
from exofile import Color, TrackBarType
from exolib import EXO, ObjectNode, TextParamNode, ImageParamNode, StandardDrawingParamNode
from unittest import TestCase 

class TestEXOSerialize (TestCase):

  def test_load (self):
    TEST_DATA = """[exedit]
width=1280
height=720
rate=24
scale=1
length=24
audio_rate=44100
audio_ch=2
[0]
layer=1
start=1
end=24
overlay=1
camera=0
[0.0]
_name=テキスト
text=b930fc30d130fc3086304b308a30bf30a430e03001ff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
autoadjust=0
soft=1
monospace=0
align=0
precision=1
color=ff0000
color2=000000
font=MS UI Gothic
サイズ=100
表示速度=0.0
文字毎に個別オブジェクト=0
移動座標上に表示する=0
自動スクロール=0
B=0
I=0
spacing_x=0
spacing_y=0
[0.1]
_name=標準描画
blend=0
X=0.0
Y=0.0
Z=0.0
拡大率=100.0
透明度=0.0
回転=0.0
[1]
layer=2
start=1
end=24
overlay=1
camera=0
[1.0]
_name=画像ファイル
file=example.png
[1.1]
_name=標準描画
blend=0
X=0.0
Y=0.0
Z=0.0
拡大率=100.0
透明度=0.0
回転=0.0
"""
    exo = EXO.loads(TEST_DATA)

    self.assertEqual(exo["width"], 1280)
    self.assertEqual(exo["height"], 720)
    self.assertEqual(exo["rate"], 24)
    self.assertEqual(exo["scale"], 1)
    self.assertEqual(exo["length"], 24)
    self.assertEqual(exo["audiorate"], 44100)
    self.assertEqual(exo["audioch"], 2)

    textobjnode = exo.find_by_position(1, 1) 
    self.assertIsInstance(textobjnode, ObjectNode)
    self.assertEqual(textobjnode["overlay"], True)
    self.assertEqual(textobjnode["camera"], False)

    textobjparamnodes = list(textobjnode.iter_objparam())
    self.assertIsInstance(textobjparamnodes[0], TextParamNode)
    self.assertEqual(textobjparamnodes[0]["text"], "スーパーゆかりタイム！")
    self.assertEqual(len(textobjparamnodes[0]["size"].values), 1)
    self.assertEqual(textobjparamnodes[0]["size"].values[0], 100)
    self.assertEqual(textobjparamnodes[0]["size"].trackbartype, TrackBarType.NONE)
    self.assertEqual(len(textobjparamnodes[0]["displayspeed"].values), 1)
    self.assertEqual(textobjparamnodes[0]["displayspeed"].values[0], 0.0)
    self.assertEqual(textobjparamnodes[0]["displayspeed"].trackbartype, TrackBarType.NONE)
    self.assertEqual(textobjparamnodes[0]["indivisualobject"], False)
    self.assertEqual(textobjparamnodes[0]["displayontranslatedposition"], False)
    self.assertEqual(textobjparamnodes[0]["autoscroll"], False)
    self.assertEqual(textobjparamnodes[0]["bold"], False)
    self.assertEqual(textobjparamnodes[0]["italic"], False)
    self.assertEqual(textobjparamnodes[0]["autoadjust"], False)
    self.assertEqual(textobjparamnodes[0]["soft"], True)
    self.assertEqual(textobjparamnodes[0]["monospace"], False)
    self.assertEqual(textobjparamnodes[0]["align"], False)
    self.assertEqual(textobjparamnodes[0]["spacingx"], 0)
    self.assertEqual(textobjparamnodes[0]["spacingy"], 0)
    self.assertEqual(textobjparamnodes[0]["precision"], True)
    self.assertEqual(textobjparamnodes[0]["color"], Color(255, 0, 0))
    self.assertEqual(textobjparamnodes[0]["color2"], Color(0, 0, 0))
    self.assertEqual(textobjparamnodes[0]["font"], "MS UI Gothic")
    self.assertIsInstance(textobjparamnodes[1], StandardDrawingParamNode)
    self.assertEqual(textobjparamnodes[1]["blend"], 0)
    self.assertEqual(len(textobjparamnodes[1]["x"].values), 1)
    self.assertEqual(textobjparamnodes[1]["x"].values[0], 0.0)
    self.assertEqual(textobjparamnodes[1]["x"].trackbartype, TrackBarType.NONE)
    self.assertEqual(len(textobjparamnodes[1]["y"].values), 1)
    self.assertEqual(textobjparamnodes[1]["y"].values[0], 0.0)
    self.assertEqual(textobjparamnodes[1]["y"].trackbartype, TrackBarType.NONE)
    self.assertEqual(len(textobjparamnodes[1]["z"].values), 1)
    self.assertEqual(textobjparamnodes[1]["z"].values[0], 0.0)
    self.assertEqual(textobjparamnodes[1]["z"].trackbartype, TrackBarType.NONE)
    self.assertEqual(len(textobjparamnodes[1]["scale"].values), 1)
    self.assertEqual(textobjparamnodes[1]["scale"].values[0], 100.0)
    self.assertEqual(textobjparamnodes[1]["scale"].trackbartype, TrackBarType.NONE)
    self.assertEqual(len(textobjparamnodes[1]["rotation"].values), 1)
    self.assertEqual(textobjparamnodes[1]["rotation"].values[0], 0.0)
    self.assertEqual(textobjparamnodes[1]["rotation"].trackbartype, TrackBarType.NONE)

    dumpedtext = exo.dumps()
    self.assertEqual(set(TEST_DATA.strip().split("\n") + ["audio=0", "type=0"]), set(dumpedtext.strip().split("\n"))) #TextParamNodeはtypeを自動的に付与します。ObjectNodeはaudioを自動的に付与します。よって雑ですが比較を行うためにTEXT_DATAにも同様の値を付与しています。

  def test_load_with_merge (self):
    TEST_DATA = """[exedit]
width=1280
height=720
rate=24
scale=1
length=72
audio_rate=44100
audio_ch=2
[0]
start=1
end=36
layer=1
overlay=1
camera=0
[0.0]
_name=図形
サイズ=0,100,103
縦横比=0.0
ライン幅=4000
type=1
color=ffffff
name=
[0.1]
_name=標準描画
X=0.0
Y=0.0
Z=0.0
拡大率=100.00
透明度=0.0
回転=0.00
blend=0
[1]
start=37
end=72
layer=1
overlay=1
camera=0
chain=1
[1.0]
_name=図形
サイズ=100,0,103
縦横比=0.0
ライン幅=4000
[1.1]
_name=標準描画
X=0.0
Y=0.0
Z=0.0
拡大率=100.00
透明度=0.0
回転=0.00
"""
    exo = EXO.loads(TEST_DATA)

    self.assertEqual(exo["width"], 1280)
    self.assertEqual(exo["height"], 720)
    self.assertEqual(exo["rate"], 24)
    self.assertEqual(exo["scale"], 1)
    self.assertEqual(exo["length"], 72)
    self.assertEqual(exo["audiorate"], 44100)
    self.assertEqual(exo["audioch"], 2)

    objnodes = list(exo.iter_layer_object(1))
    self.assertEqual(len(objnodes), 1)
    self.assertEqual(objnodes[0].positionrange.start, 1)
    self.assertEqual(objnodes[0].positionrange.end, 72)
    self.assertEqual(objnodes[0]["overlay"], True)
    self.assertEqual(objnodes[0]["camera"], False)

    objparamnodes = list(objnodes[0].iter_objparam())
    self.assertEqual(len(objparamnodes), 2)
    self.assertEqual(len(objparamnodes[0]["size"].values), 3)
    self.assertEqual(objparamnodes[0]["size"].values[0], 0)
    self.assertEqual(objparamnodes[0]["size"].values[1], 100)
    self.assertEqual(objparamnodes[0]["size"].values[2], 0)
    self.assertEqual(objparamnodes[0]["size"].accelerate, True)
    self.assertEqual(objparamnodes[0]["size"].decelerate, True)
    self.assertEqual(objparamnodes[0]["size"].parameter, None)
    self.assertEqual(len(objparamnodes[0]["aspect"].values), 1)
    self.assertEqual(objparamnodes[0]["aspect"].values[0], 0.0)
    self.assertEqual(len(objparamnodes[0]["linewidth"].values), 1)
    self.assertEqual(objparamnodes[0]["linewidth"].values[0], 4000)
    self.assertEqual(objparamnodes[0]["color"], Color(255, 255, 255))
    self.assertEqual(objparamnodes[0]["name"], "")
    self.assertEqual(len(objparamnodes[1]["x"].values), 1)
    self.assertEqual(objparamnodes[1]["x"].values[0], 0.0)
    self.assertEqual(objparamnodes[1]["x"].trackbartype, TrackBarType.NONE)
    self.assertEqual(len(objparamnodes[1]["y"].values), 1)
    self.assertEqual(objparamnodes[1]["y"].values[0], 0.0)
    self.assertEqual(objparamnodes[1]["y"].trackbartype, TrackBarType.NONE)
    self.assertEqual(len(objparamnodes[1]["z"].values), 1)
    self.assertEqual(objparamnodes[1]["z"].values[0], 0.0)
    self.assertEqual(objparamnodes[1]["z"].trackbartype, TrackBarType.NONE)
    self.assertEqual(len(objparamnodes[1]["scale"].values), 1)
    self.assertEqual(objparamnodes[1]["scale"].values[0], 100.00)
    self.assertEqual(objparamnodes[1]["scale"].trackbartype, TrackBarType.NONE)
    self.assertEqual(len(objparamnodes[1]["transparent"].values), 1)
    self.assertEqual(objparamnodes[1]["transparent"].values[0], 0.0)
    self.assertEqual(objparamnodes[1]["transparent"].trackbartype, TrackBarType.NONE)
    self.assertEqual(len(objparamnodes[1]["rotation"].values), 1)
    self.assertEqual(objparamnodes[1]["rotation"].values[0], 0.00)
    self.assertEqual(objparamnodes[1]["rotation"].trackbartype, TrackBarType.NONE)
    self.assertEqual(objparamnodes[1]["blend"], 0)

    dumpedtext = exo.dumps()
    self.assertEqual(set(TEST_DATA.strip().split("\n") + ["audio=0"]), set(dumpedtext.strip().split("\n"))) #ObjectNodeはaudioを自動的に付与します。よって雑ですが比較を行うためにTEXT_DATAにも同様の値を付与しています。
