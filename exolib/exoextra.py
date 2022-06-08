
from exofile import Color, Text, String, Float, Int, Boolean, Param, ShapeType, ShapeName
from .object_node import ObjectNode
from .object_param_node import ObjectParamNode
from .serializable_multi_value import IntTrackBarRanges, FloatTrackBarRanges

class VideoParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("file", "file"): String, 
    ("再生位置", "playbackposition"): FloatTrackBarRanges, 
    ("再生速度", "playbackspeed"): FloatTrackBarRanges, 
    ("ループ再生", "loopplayback"): Boolean, 
    ("アルファチャンネルを読み込む", "usealphachannel"): Boolean, 
  }

  def __init__ (self, file, *, playbackposition=1, playbackspeed=100.0, loopplayback=False, usealphachannel=False, **params):
    super().__init__(**params | { 
      "_name": "動画ファイル",
      "file": file,
      "playbackposition": playbackposition,
      "playbackspeed": playbackspeed,
      "loopplayback": loopplayback,
      "usealphachannel": usealphachannel,  
    })

class StandardDrawingParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("X", "x"): FloatTrackBarRanges,
    ("Y", "y"): FloatTrackBarRanges,
    ("Z", "z"): FloatTrackBarRanges,
    ("拡大率", "scale"): FloatTrackBarRanges,
    ("透明度", "transparent"): FloatTrackBarRanges,
    ("回転", "rotation"): FloatTrackBarRanges,
    ("blend", "blend"): Int,
  }

  def __init__ (self, x, y, z, *, scale=100.0, transparent=0.0, rotation=0.0, blend=0, **params):
    super().__init__(**params | { 
      "_name": "標準描画",
      "x": x,
      "y": y,
      "z": z,
      "scale": scale,
      "transparent": transparent,
      "rotation": rotation,
      "blend": blend,
    })

class ImageParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("file", "file"): String,
  }

  def __init__ (self, file, **params):
    super().__init__(**params | { 
      "_name": "画像ファイル",
      "file": file,
    })

class AudioParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("file", "file"): String, 
    ("再生位置", "playbackposition"): FloatTrackBarRanges, 
    ("再生速度", "playbackspeed"): FloatTrackBarRanges, 
    ("ループ再生", "loopplayback"): Boolean, 
    ("動画ファイルと連携", "linkwithvideo"): Boolean, 
  }

  def __init__ (self, file, *, playbackposition=0.00, playbackspeed=100.0, loopplayback=False, linkwithvideo=False, **params):
    super().__init__(**params | { 
      "_name": "音声ファイル",
      "file": file,
      "playbackposition": playbackposition,
      "playbackspeed": playbackspeed,
      "loopplayback": loopplayback,
      "linkwithvideo": linkwithvideo,  
    })

class StandardPlayingParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("音量", "volume"): FloatTrackBarRanges, 
    ("左右", "direction"): FloatTrackBarRanges, 
  }

  def __init__ (self, *, volume=100.0, direction=0.0, **params):
    super().__init__(**params | { 
      "_name": "標準再生",
      "volume": volume,
      "direction": direction,  
    })

class TextParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("text", "text"): Text, 
    ("サイズ", "size"): IntTrackBarRanges, 
    ("表示速度", "displayspeed"): FloatTrackBarRanges, 
    ("文字毎に個別オブジェクト", "indivisualobject"): Boolean, 
    ("移動座標上に表示する", "displayontranslatedposition"): Boolean, 
    ("自動スクロール", "autoscroll"): Boolean, 
    ("B", "bold"): Boolean, 
    ("I", "italic"): Boolean, 
    ("autoadjust", "autoadjust"): Boolean, 
    ("soft", "soft"): Boolean, 
    ("monospace", "monospace"): Boolean, 
    ("align", "align"): Int, 
    ("type", "type"): Int, 
    ("spacing_x", "spacingx"): Int, 
    ("spacing_y", "spacingy"): Int, 
    ("precision", "precision"): Boolean, 
    ("color", "color"): Color, 
    ("color2", "color2"): Color, 
    ("font", "font"): String, 
  }

  def __init__ (self, text, *, size=34, displayspeed=0.0, indivisualobject=False, displayontranslatedposition=False, autoscroll=False, bold=False, italic=False, autoadjust=False, soft=True, monospace=False, align=0, type=0, spacingx=0, spacingy=0, precision=True, color=Color(255, 255, 255), color2=Color(0, 0, 0), font="MS UI Gothic", **params):
    super().__init__(**params | { 
      "_name": "テキスト",
      "text": text,
      "size": size,
      "displayspeed": displayspeed,
      "indivisualobject": indivisualobject,
      "displayontranslatedposition": displayontranslatedposition,
      "autoscroll": autoscroll,
      "bold": bold,
      "italic": italic,
      "autoadjust": autoadjust,
      "soft": soft,
      "monospace": monospace,
      "align": align,
      "type": type,
      "spacingx": spacingx,
      "spacingy": spacingy,
      "precision": precision,
      "color": color,
      "color2": color2,
      "font": font,  
    })

class ShapeParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("type", "type"): Int,
    ("サイズ", "size"): IntTrackBarRanges,
    ("縦横比", "aspect"): FloatTrackBarRanges,
    ("ライン幅", "linewidth"): IntTrackBarRanges,
    ("color", "color"): Color,
    ("name", "name"): ShapeName,
  }

  def __init__ (self, type=ShapeType.CIRCLE, *, size=100, aspect=0.0, linewidth=4000, color=Color(255, 255, 255), name="", **params):
    super().__init__(**params | { 
      "_name": "図形",
      "type": type,
      "size": size,
      "aspect": aspect,
      "linewidth": linewidth,
      "color": color,
      "name": name,  
    })

class FrameBufferParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("フレームバッファをクリア", "clear"): Boolean, 
  }

  def __init__ (self, *, clear=False, **params):
    super().__init__(**params | { 
      "_name": "フレームバッファ",
      "clear": clear,
    })

class SoundWaveParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("横幅", "width"): IntTrackBarRanges, 
    ("高さ", "height"): IntTrackBarRanges, 
    ("音声", "volume"): FloatTrackBarRanges, 
    ("再生位置", "playbackposition"): FloatTrackBarRanges, 
    ("編集全体の音声を元にする", "referencescenesound"): Boolean, 
    ("file", "file"): String, 
    ("type", "type"): Int, 
    ("mode", "mode"): Int, 
    ("res_w", "resw"): Int, 
    ("res_h", "resh"): Int, 
    ("pad_w", "padw"): Int, 
    ("pad_h", "padh"): Int, 
    ("color", "color"): Color, 
    ("sample_n", "samplen"): Int, 
    ("mirror", "mirror"): Int, 
  }

  def __init__ (self, width=640, height=240, *, volume=100.0, playbackposition=0.0, referencescenesound=True, file="", type=0, mode=0, resw=0, resh=4096, padw=0, padh=0, color=Color(255, 255, 255), samplen=0, mirror=0, **params):
    super().__init__(**params | { 
      "_name": "音声波形表示",
      "width": width,
      "height": height,
      "volume": volume,
      "playbackposition": playbackposition,
      "referencescenesound": referencescenesound,
      "file": file,
      "type": type,
      "mode": mode,
      "resw": resw,
      "resh": resh,
      "padw": padw,
      "padh": padh,
      "color": color,
      "samplen": samplen,
      "mirror": mirror, 
    })

class SceneParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("", "scene"): Int,
    ("再生位置","playbackposition"): FloatTrackBarRanges,
    ("再生速度","playbackspeed"): FloatTrackBarRanges,
    ("ループ再生", "loopplayback"): Boolean,
  }

  def __init__ (self, scene, *, playbackposition=1, playbackspeed=100.0, loopplayback=False, **params):
    super().__init__(**params | { 
      "_name": "シーン",
      "scene": scene,
      "playbackposition": playbackposition,
      "playbackspeed": playbackspeed,
      "loopplayback": loopplayback,
    })

class PreviousObjectParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
  }

  def __init__ (self, **params):
    super().__init__(**params | {
      "_name": "直前のオブジェクト",
    })
 
class ExpansionDrawingParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("X", "x"): FloatTrackBarRanges, 
    ("Y", "y"): FloatTrackBarRanges, 
    ("Z", "z"): FloatTrackBarRanges, 
    ("拡大率", "scale"): FloatTrackBarRanges, 
    ("透明度", "transparent"): FloatTrackBarRanges, 
    ("縦横比", "aspect"): FloatTrackBarRanges, 
    ("X軸回転", "rotationx"): FloatTrackBarRanges, 
    ("Y軸回転", "rotationy"): FloatTrackBarRanges, 
    ("Z軸回転", "rotationz"): FloatTrackBarRanges, 
    ("中心X", "centerx"): FloatTrackBarRanges, 
    ("中心Y", "centery"): FloatTrackBarRanges, 
    ("中心Z", "centerz"): FloatTrackBarRanges, 
    ("裏面を表示しない", "hidebackside"): Boolean, 
    ("blend", "blend"): Int, 
  }

  def __init__ (self, x, y, z, *, scale=100.0, transparent=0.0, aspect=0.0, rotationx=0.0, rotationy=0.0, rotationz=0.0, centerx=0.0, centery=0.0, centerz=0.0, hidebackside=False, blend=0, **params):
    super().__init__(**params | { 
      "_name": "拡張描画",
      "x": x,
      "y": y,
      "z": z,
      "scale": scale,
      "transparent": transparent,
      "aspect": aspect,
      "rotationx": rotationx,
      "rotationy": rotationy,
      "rotationz": rotationz,
      "centerx": centerx,
      "centery": centery,
      "centerz": centerz,
      "hidebackside": hidebackside,
      "blend": blend,
    })

class ParticleParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("X", "x"): FloatTrackBarRanges, 
    ("Y", "y"): FloatTrackBarRanges, 
    ("Z", "z"): FloatTrackBarRanges, 
    ("出力頻度", "outputfrequency"): FloatTrackBarRanges, 
    ("出力速度", "outputspeed"): FloatTrackBarRanges, 
    ("加速度", "acceleration"): FloatTrackBarRanges, 
    ("出力方向", "outputdirection"): FloatTrackBarRanges, 
    ("拡散角度", "spreadingangle"): FloatTrackBarRanges, 
    ("透過率", "transparent"): FloatTrackBarRanges, 
    ("透過速度", "transparentspeed"): FloatTrackBarRanges, 
    ("拡大率", "scale"): FloatTrackBarRanges, 
    ("拡大速度", "scalespeed"): FloatTrackBarRanges, 
    ("回転角", "angle"): FloatTrackBarRanges, 
    ("回転速度", "anglespeed"): FloatTrackBarRanges, 
    ("重力", "gravity"): FloatTrackBarRanges, 
    ("生存時間", "lifespan"): FloatTrackBarRanges, 
    ("出力方向の基準を移動方向にする", "referencemovementdirectiontooutputdirection"): Boolean, 
    ("移動範囲の座標からランダムに出力", "randomoutputfrommovementrange"): Boolean, 
    ("3Dランダム回転", "random3drotation"): Boolean, 
    ("終了点で全て消えるように調節する", "adjusttodisappearsatendpoint"): Boolean, 
    ("blend", "blend"): Int, 
  }

  def __init__ (self, x, y, z, *, outputfrequency=20.0, outputspeed=400.0, acceleration=0.0, outputdirection=0.0, spreadingangle=30.0, transparent=0.0, transparentspeed=0.0, scale=100.00, scalespeed=0.00, angle=0.00, anglespeed=0.00, gravity=0.0, lifespan=0.0, referencemovementdirectiontooutputdirection=False, randomoutputfrommovementrange=False, random3drotation=False, adjusttodisappearsatendpoint=True, blend=0, **params):
    super().__init__(**params | { 
      "_name": "パーティクル出力",
      "x": x,
      "y": y,
      "z": z,
      "outputfrequency": outputfrequency,
      "outputspeed": outputspeed,
      "acceleration": acceleration,
      "outputdirection": outputdirection,
      "spreadingangle": spreadingangle,
      "transparent": transparent,
      "transparentspeed": transparentspeed,
      "scale": scale,
      "scalespeed": scalespeed,
      "angle": angle,
      "anglespeed": anglespeed,
      "gravity": gravity,
      "lifespan": lifespan,
      "referencemovementdirectiontooutputdirection": referencemovementdirectiontooutputdirection,
      "randomoutputfrommovementrange": randomoutputfrommovementrange,
      "random3drotation": random3drotation,
      "adjusttodisappearsatendpoint": adjusttodisappearsatendpoint,
      "blend": blend,
    })

class CustomObjectParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("track0", "track0"): FloatTrackBarRanges,
    ("track1", "track1"): FloatTrackBarRanges,
    ("track2", "track2"): FloatTrackBarRanges,
    ("track3", "track3"): FloatTrackBarRanges,
    ("check0", "check0"): Int, #0 or 100.
    ("type", "type"): Int,
    ("filter", "filter"): Int,
    ("name", "name"): String,
    ("param", "param"): Param,
  }

  def __init__ (self, name, track0=0, track1=0, track2=0, track3=0, *, check0=False, type=0, filter=0, param={}, **params):
    super().__init__(**params | {
      "_name": "カスタムオブジェクト",
      "track0": track0,
      "track1": track1,
      "track2": track2,
      "track3": track3,
      "check0": check0,
      "type": type,
      "filter": filter,
      "name": name,
      "param": param,
    })

class AnimationEffectObjectParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("track0", "track0"): FloatTrackBarRanges,
    ("track1", "track1"): FloatTrackBarRanges,
    ("track2", "track2"): FloatTrackBarRanges,
    ("track3", "track3"): FloatTrackBarRanges,
    ("check0", "check0"): Int, #0 or 100.
    ("type", "type"): Int,
    ("filter", "filter"): Int,
    ("name", "name"): String,
    ("param", "param"): Param,
  }

  def __init__ (self, name, track0=0, track1=0, track2=0, track3=0, *, check0=False, type=0, filter=0, param={}, **params):
    super().__init__(**params | {
      "_name": "アニメーション効果",
      "track0": track0,
      "track1": track1,
      "track2": track2,
      "track3": track3,
      "check0": check0,
      "type": type,
      "filter": filter,
      "name": name,
      "param": param,
    })

class GroupObjectParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("X", "x"): FloatTrackBarRanges,
    ("Y", "y"): FloatTrackBarRanges,
    ("Z", "z"): FloatTrackBarRanges,
    ("拡大率", "scale"): FloatTrackBarRanges,
    ("X軸回転", "rotationx"): FloatTrackBarRanges,
    ("Y軸回転", "rotationy"): FloatTrackBarRanges,
    ("Z軸回転", "rotationz"): FloatTrackBarRanges,
    ("上位グループ制御の影響を受ける", "affectedbyupperlayer"): Boolean,
    ("同じグループのオブジェクトを対象にする", "targetsamegroupobjs"): Boolean,
    ("range", "range"): Int,
  }

  def __init__ (self, x, y, z, *, scale=100.0, rotationx=0.0, rotationy=0.0, rotationz=0.0, affectedbyupperlayer=False, targetsamegroupobjs=True, range=0, **params):
    super().__init__(**params | {
      "_name": "グループ制御",
      "x": x, 
      "y": y, 
      "z": z, 
      "scale": scale, 
      "rotationx": rotationx, 
      "rotationy": rotationy, 
      "rotationz": rotationz, 
      "affectedbyupperlayer": affectedbyupperlayer, 
      "targetsamegroupobjs": targetsamegroupobjs, 
      "range": range, 
    })

#その他未実装のオブジェクトを実装する
