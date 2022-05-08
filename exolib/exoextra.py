
from exofile import Color, Text, String, Float, Int, Boolean
from .object_node import ObjectNode
from .object_param_node import ObjectParamNode

class VideoParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("file", "file"): String, 
    ("再生位置", "playbackposition"): Float, 
    ("再生速度", "playbackspeed"): Float, 
    ("ループ再生", "loopplayback"): Boolean, 
    ("アルファチャンネルを読み込む", "usealphachannel"): Boolean, 
  }

  def __init__ (self, file, *, playbackposition=1, playbackspeed=100.0, loopplayback=False, usealphachannel=False, **params):
    super().__init__("動画ファイル", **params | {
      "file": file,
      "playbackposition": playbackposition,
      "playbackspeed": playbackspeed,
      "loopplayback": loopplayback,
      "usealphachannel": usealphachannel,  
    })

class StandardDrawingParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("X", "x"): Float,
    ("Y", "y"): Float,
    ("Z", "z"): Float,
    ("拡大率", "scale"): Float,
    ("透明度", "transparent"): Float,
    ("回転", "rotation"): Float,
    ("blend", "blend"): Int,
  }

  def __init__ (self, x, y, z, *, scale=100.0, transparent=0.0, rotation=0.0, blend=0, **params):
    super().__init__("標準描画", **params | {
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
    super().__init__("画像ファイル", **params | {
      "file": file,
    })

class AudioParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("file", "file"): String, 
    ("再生位置", "playbackposition"): Float, 
    ("再生速度", "playbackspeed"): Float, 
    ("ループ再生", "loopplayback"): Boolean, 
    ("動画ファイルと連携", "linkwithvideo"): Boolean, 
  }

  def __init__ (self, file, *, playbackposition=0.00, playbackspeed=100.0, loopplayback=False, linkwithvideo=False, **params):
    super().__init__("音声ファイル", **params | {
      "file": file,
      "playbackposition": playbackposition,
      "playbackspeed": playbackspeed,
      "loopplayback": loopplayback,
      "linkwithvideo": linkwithvideo,  
    })

class StandardPlayingParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("音量", "volume"): Float, 
    ("左右", "direction"): Float, 
  }

  def __init__ (self, *, volume=100.0, direction=0.0, **params):
    super().__init__("標準再生", **params | {
      "volume": volume,
      "direction": direction,  
    })

class TextParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("text", "text"): Text, 
    ("サイズ", "size"): Int, 
    ("表示速度", "displayspeed"): Float, 
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
    super().__init__("テキスト", **params | {
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
    ("サイズ", "size"): Int,
    ("縦横比", "aspect"): Float,
    ("ライン幅", "linewidth"): Int,
    ("color", "color"): Color,
    ("name", "name"): String,
  }

  def __init__ (self, type=1, *, size=100, aspect=0.0, linewidth=4000, color="ffffff", name="", **params):
    super().__init__("図形", **params | {
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
    super().__init__("フレームバッファ", **params | {
      "clear": clear,
    })

class SoundWaveParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("横幅", "width"): Int, 
    ("高さ", "height"): Int, 
    ("音声", "volume"): Float, 
    ("再生位置", "playbackposition"): Float, 
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

  def __init__ (self, width=640, height=240, *, volume=100.0, playbackposition=0.0, referencescenesound=True, file="", type=0, mode=0, resw=0, resh=4096, padw=0, padh=0, color="ffffff", samplen=0, mirror=0, **params):
    super().__init__("音声波形表示", **params | {
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
    ("再生位置","playbackposition"): Float,
    ("再生速度","playbackspeed"): Float,
    ("ループ再生", "loopplayback"): Boolean,
  }

  def __init__ (self, scene, *, playbackposition=1, playbackspeed=100.0, loopplayback=False, **params):
    super().__init__("シーン", **params | {
      "scene": scene,
      "playbackposition": playbackposition,
      "playbackspeed": playbackspeed,
      "loopplayback": loopplayback,
    })

class PreviousObjectParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
  }

  def __init__ (self, **params):
    super().__init__("直前のオブジェクト", **params)

class ExpansionDrawingParamNode (ObjectParamNode):

  transformation_table = ObjectParamNode.transformation_table | {
    ("X", "x"): Float, 
    ("Y", "y"): Float, 
    ("Z", "z"): Float, 
    ("拡大率", "scale"): Float, 
    ("透明度", "transparent"): Float, 
    ("縦横比", "aspect"): Float, 
    ("X軸回転", "rotationx"): Float, 
    ("Y軸回転", "rotationy"): Float, 
    ("Z軸回転", "rotationz"): Float, 
    ("中心X", "centerx"): Float, 
    ("中心Y", "centery"): Float, 
    ("中心Z", "centerz"): Float, 
    ("裏面を表示しない", "hidebackside"): Boolean, 
    ("blend", "blend"): Int, 
  }

  def __init__ (self, x, y, z, *, scale=100.0, transparent=0.0, aspect=0.0, rotationx=0.0, rotationy=0.0, rotationz=0.0, centerx=0.0, centery=0.0, centerz=0.0, hidebackside=False, blend=0, **params):
    super().__init__("拡張描画", **params | {
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
    ("X", "x"): Float, 
    ("Y", "y"): Float, 
    ("Z", "z"): Float, 
    ("出力頻度", "outputfrequency"): Float, 
    ("出力速度", "outputspeed"): Float, 
    ("加速度", "acceleration"): Float, 
    ("出力方向", "outputdirection"): Float, 
    ("拡散角度", "spreadingangle"): Float, 
    ("透過率", "transparent"): Float, 
    ("透過速度", "transparentspeed"): Float, 
    ("拡大率", "scale"): Float, 
    ("拡大速度", "scalespeed"): Float, 
    ("回転角", "angle"): Float, 
    ("回転速度", "anglespeed"): Float, 
    ("重力", "gravity"): Float, 
    ("生存時間", "lifespan"): Float, 
    ("出力方向の基準を移動方向にする", "shutsuryokuhoukounokijyunnwoidouhoukounisuru"): Boolean, 
    ("移動範囲の座標からランダムに出力", "idouhanninozahyoukararandomnishuturyoku"): Boolean, 
    ("3Dランダム回転", "random3drotation"): Boolean, 
    ("終了点で全て消えるように調節する", "shuuryoutenndesubetekieruyounityousetsusuru"): Boolean, 
    ("blend", "blend"): Float, 
  }

  def __init__ (self, x, y, z, *, outputfrequency=20.0, outputspeed=400.0, acceleration=0.0, outputdirection=0.0, spreadingangle=30.0, transparent=0.0, transparentspeed=0.0, scale=100.00, scalespeed=0.00, angle=0.00, anglespeed=0.00, gravity=0.0, lifespan=0.0, shutsuryokuhoukounokijyunnwoidouhoukounisuru=False, idouhanninozahyoukararandomnishuturyoku=False, random3drotation=False, shuuryoutenndesubetekieruyounityousetsusuru=True, blend=0, **params):
    super().__init__("パーティクル出力", **params | {
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
      "shutsuryokuhoukounokijyunnwoidouhoukounisuru": shutsuryokuhoukounokijyunnwoidouhoukounisuru,
      "idouhanninozahyoukararandomnishuturyoku": idouhanninozahyoukararandomnishuturyoku,
      "random3drotation": random3drotation,
      "shuuryoutenndesubetekieruyounityousetsusuru": shuuryoutenndesubetekieruyounityousetsusuru,
      "blend": blend,
    })

#カスタムオブジェクト、グループ制御などなどを実装する
