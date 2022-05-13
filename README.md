
# exolib

![](https://img.shields.io/badge/version-0.11.0-gray)
![](https://img.shields.io/badge/python-3.10-blue)
![](https://img.shields.io/github/license/tikubonn/exolib)

AviUtlのエクスポートファイルを編集できるライブラリです。
既存のファイルを編集するだけに限らず、新たなファイルを新規作成することもできます。
このライブラリを使うことで、例えば会話文から感情を推論させて、感情に沿った立ち絵・文章・音声を配置した.exoファイルを作成する。
なんてこともできるかもしれないですね。

ただしこのライブラリは「高速で動くよりとりあえず動くもの」をコンセプトに書いたため実行速度はそれほど速くありません。
さらに多くの検索処理が線形探索なので大量のオブジェクトを配置すると重くなる可能性がございます。
自分はとりあえず動くのがわかって満足なので、もっと高速なものが欲しい人は自分で書くなりしていただきますようお願いします。

```python
from exolib import EXO

with open("example.exo", "r", encoding="cp932") as stream:
  exo = EXO.load(stream)

for layer in range(1, 99 +1):
  for obj in exo.iter_layer_object(layer):
    for key, value in obj.items():
      print(obj, key, value) #print object's entries.
    for objparam in obj.iter_objparam():
      for key, value in objparam.items():
        print(objparam, key, value) #print objparam's entries.
```

## Usage

### .exoファイルを読み込む・書き出す

`EXO.load`クラスメソッドを使用することでファイルを読み込むことができます。
`EXO.dump`メソッドを使用することでファイルにインスタンスを書き出すことができます。
ファイルの読み込み・書き出しともに文字コードの指定には注意しましょう。
.exoファイルは基本的に**cp932**でエンコードされています。

```python
from exolib import EXO

with open("example.exo", "r", encoding="cp932") as stream:
  exo = EXO.load(stream)

for obj in exo.iter_layer_object(1):
  exo.remove_object(obj)

with open("example2.exo", "w", encoding="cp932") as stream:
  exo.fit_length_to_last_object()
  exo.dump(stream)
```

### .exoファイルを文字列から読み込む・書き出す

exolibは文字列化されたファイルからも読み込む・書き込むことができます。
文字列化されたファイルを読み込むには`EXO.loads`クラスメソッドを使用します。
逆にインスタンスを文字列に書き出すには`EXO.dumps`メソッドを使用します。

```python
from exolib import EXO

with open("example.exo", "r", encoding="cp932") as stream:
  data = stream.read()

exo = EXO.loads(data) #load from str.

for obj in exo.iter_layer_object(1):
  exo.remove_object(obj)

exo.dumps(stream) #dump to stdout if run on REPL.
```

### .exoファイルを新規作成する

exolibは既存のファイルから読み込むだけでなく、.exoファイルを新規作成することもできます。

```python
from exolib import EXO, ObjectNode, TextParamNode, StandardDrawingParamNode, PositionRange, InsertionMode

with open("example3.exo", "w", encoding="cp932") as stream:
  exo = EXO(width=1280, height=720, rate=24)
  exo.dump(stream)
```

### テキストオブジェクトを追加する

exolibはタイムラインを編集することもできます。
試しに新規作成したファイルにテキストオブジェクトを追加してみましょう。
テキストオブジェクトを構成する最小限の要素はこのようになります。

* ObjectNode (オブジェクト本体)
* TextParamNode (テキスト関連のパラメータ)
* StandardDrawingParamNode (標準描画関連のパラメータ)

これらのインスタンスを作成後、各種パラメータノードを`ObjectNode`インスタンスに追加します。
これでテキストオブジェクトの準備ができました。

最後にテキストオブジェクトをタイムラインに追加しましょう。
オブジェクトをタイムラインに追加するには`EXO.insert_object`メソッドを使用します。
引数の最後は`InsertionMode.SHIFT_RIGHT`にします。
この挿入モードは既に挿入先にオブジェクトが存在していた場合、右側の空いている場所を検索し再挿入を試みます。

```python
from exolib import EXO, ObjectNode, TextParamNode, StandardDrawingParamNode, PositionRange, InsertionMode

exo = EXO()

textobj = ObjectNode()
textobj.add_objparam(TextParamNode("吾輩は猫である。")) 
textobj.add_objparam(StandardDrawingParamNode(0, -100, 0))
exo.insert_object(1, PositionRange(1, 24), textobj, InsertionMode.SHIFT_RIGHT) #layer1, 1 ~ 24

textobj2 = ObjectNode()
textobj2.add_objparam(TextParamNode("名前はまだ無い。")) 
textobj2.add_objparam(StandardDrawingParamNode(0, 0, 0))
exo.insert_object(1, PositionRange(1, 24), textobj2, InsertionMode.SHIFT_RIGHT) #layer1, 25 ~ 48

with open("example3.exo", "w", encoding="cp932") as stream:
  exo.fit_length_to_last_object()
  exo.dump(stream)
```

### 挿入モードの種類

exolibはこれらの挿入モードを提供しています。

| 挿入モード | 概要 | 
| ---- | ---- | 
| `InsertionMode.NONE`        | なにも行わない。既に挿入先にオブジェクトが存在していれば`InsertionError`を送出します。 | 
| `InsertionMode.DEFAULT`     | `NONE`を指定したときと同じ振る舞いをします。`EXO.insert_object`メソッドの挿入モードが未指定の時に使用されます。 | 
| `InsertionMode.SHIFT_LEFT`  | 既に挿入先にオブジェクトが存在していれば、そこから左にある空き場所に挿入を試みます。挿入可能な場所が見つからなければ`InsertionError`を送出します。 | 
| `InsertionMode.SHIFT_RIGHT` | 既に挿入先にオブジェクトが存在していれば、そこから右にある空き場所に挿入を試みます。 | 
| `InsertionMode.PUSH_LEFT`   | 既に挿入先にオブジェクトが存在していれば、そこから左にあるすべてのオブジェクトをずらし、挿入場所を確保します。左端に十分ずらせるだけの空き場所なければ`InsertionError`を送出します。 | 
| `InsertionMode.PUSH_RIGHT`  | 既に挿入先にオブジェクトが存在していれば、そこから右にあるすべてのオブジェクトをずらし、挿入場所を確保します。 | 
| `InsertionMode.OVERWRITE`   | 既に挿入先にオブジェクトが存在していれば、重なるオブジェクトすべてを切り詰め・または削除し、挿入場所を確保します。一意性の関係で、挿入範囲を超える大きさのオブジェクトが挿入場所に存在していた場合、そのオブジェクトは２分割されずそのまま右側が消失します。 | 

### トラックバーアニメーションを追加する

exolibはトラックバーアニメーションにも対応しています。
トラックバーアニメーションを使用するには`FloatTrackBarRanges`等のクラスを使用します。

```python
from exolib import EXO, ObjectNode, TextParamNode, StandardDrawingParamNode, PositionRange, InsertionMode, FloatTrackBarRanges
from exofile import TrackBarType 

exo = EXO()

textobj = ObjectNode()
textobj.add_objparam(TextParamNode("吾輩は猫である。")) 
textobj.add_objparam(StandardDrawingParamNode(
  FloatTrackBarRange((-100, 100), TrackBarType.LINEAR), 
  FloatTrackBarRange((0, 0), TrackBarType.LINEAR), 
  FloatTrackBarRange((0, 0), TrackBarType.LINEAR)
))
exo.insert_object(1, PositionRange(1, 24), textobj, InsertionMode.SHIFT_RIGHT) #layer1, 1 ~ 24

textobj2 = ObjectNode()
textobj2.add_objparam(TextParamNode("名前はまだ無い。")) 
textobj.add_objparam(StandardDrawingParamNode(
  FloatTrackBarRange((0, 0), TrackBarType.LINEAR), 
  FloatTrackBarRange((-100, 100), TrackBarType.LINEAR), 
  FloatTrackBarRange((0, 0), TrackBarType.LINEAR)
))
exo.insert_object(1, PositionRange(1, 24), textobj2, InsertionMode.SHIFT_RIGHT) #layer1, 25 ~ 48

with open("example4.exo", "w", encoding="cp932") as stream:
  exo.fit_length_to_last_object()
  exo.dump(stream)
```

### 中間点を追加する

exolibはオブジェクトの中間点にも対応しています。
オブジェクトに中間点を追加するには`ObjectNode.add_midpoint`メソッドを使用します。
中間点を追加したら、それに合わせて`FloatTrackBarRanges`のパラメーター数も増やしましょう。

```python
from exolib import EXO, ObjectNode, TextParamNode, StandardDrawingParamNode, PositionRange, InsertionMode, FloatTrackBarRanges
from exofile import TrackBarType, TextAlignment

exo = EXO()

textobj = ObjectNode()
textobj.add_objparam(TextParamNode("吾輩は猫である。", align=TextAlignment.ALIGN_CENTER_MIDDLE)) 
textobj.add_objparam(StandardDrawingParamNode(
  FloatTrackBarRanges((-100, 100, -100), TrackBarType.LINEAR), 
  FloatTrackBarRanges((0, 0, 0), TrackBarType.LINEAR), 
  FloatTrackBarRanges((0, 0, 0), TrackBarType.LINEAR)
))
textobj.add_midpoint(24)
exo.insert_object(1, PositionRange(1, 48), textobj, InsertionMode.SHIFT_RIGHT) #layer1, 1 ~ 24

with open("example5.exo", "w", encoding="cp932") as stream:
  exo.fit_length_to_last_object()
  exo.dump(stream)
```

### 音声オブジェクトを追加する 

最後に音声オブジェクトも追加してみましょう。
音声オブジェクトを構成する最小限の要素はこのようになります。

* ObjectNode (オブジェクト本体)
* AudioParamNode (音声ファイル関連のパラメータ)
* StandardPlayingParamNode (標準再生関連のパラメータ)

これらのインスタンスを作成後、各種パラメータノードを`ObjectNode`インスタンスに追加します。
ただし`ObjectNode`を作成する際には`audio=True`することを忘れないようにしましょう。
これで音声オブジェクトの準備ができました。
あとはテキストオブジェクトと同様に挿入処理を行うだけです。

```python
from exolib import EXO, ObjectNode, AudioParamNode, StandardPlayingParamNode, PositionRange, InsertionMode

exo = EXO()

audioobj = ObjectNode(audio=True)
audioobj.add_objparam(AudioParamNode("example.wav")) 
audioobj.add_objparam(StandardPlayingParamNode(volume=100.0, direction=-100.0))
exo.insert_object(1, PositionRange(1, 24), audioobj, InsertionMode.SHIFT_RIGHT)

audioobj2 = ObjectNode(audio=True)
audioobj2.add_objparam(AudioParamNode("example.wav")) 
audioobj2.add_objparam(StandardPlayingParamNode(volume=100.0, direction=100.0))
exo.insert_object(1, PositionRange(1, 24), audioobj2, InsertionMode.SHIFT_RIGHT)

with open("example6.exo", "w", encoding="cp932") as stream:
  exo.fit_length_to_last_object()
  exo.dump(stream)
```

## Package requirements

* exofile: https://github.com/tikubonn/exofile

## Install

```
python setup.py install
```

```
python setup.py test
```

## License 

The MIT License.

## Copyright 

exofile: The MIT License &copy; 2022 tikubonn. All Rights Reserved.
