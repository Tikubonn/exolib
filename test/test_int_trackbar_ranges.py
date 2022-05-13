
from unittest import TestCase 
from exolib import IntTrackBarRanges
from exofile import IntTrackBarRange, TrackBarType

class TestIntTrackBarRanges (TestCase):

  def test_deserialize (self):

    #without parameter

    trackrange = IntTrackBarRanges.deserialize("-100,100,1")
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100)
    self.assertEqual(trackrange.values[1], 100)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, False)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, None)

    trackrange = IntTrackBarRanges.deserialize("-100,100,65")
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100)
    self.assertEqual(trackrange.values[1], 100)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, True)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, None)

    trackrange = IntTrackBarRanges.deserialize("-100,100,33")
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100)
    self.assertEqual(trackrange.values[1], 100)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, False)
    self.assertEqual(trackrange.decelerate, True)
    self.assertEqual(trackrange.parameter, None)

    trackrange = IntTrackBarRanges.deserialize("-100,100,97")
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100)
    self.assertEqual(trackrange.values[1], 100)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, True)
    self.assertEqual(trackrange.decelerate, True)
    self.assertEqual(trackrange.parameter, None)

    #with parameter

    trackrange = IntTrackBarRanges.deserialize("-100,100,1,100")
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100)
    self.assertEqual(trackrange.values[1], 100)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, False)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, 100)

    trackrange = IntTrackBarRanges.deserialize("-100,100,65,100")
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100)
    self.assertEqual(trackrange.values[1], 100)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, True)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, 100)

    trackrange = IntTrackBarRanges.deserialize("-100,100,33,100")
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100)
    self.assertEqual(trackrange.values[1], 100)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, False)
    self.assertEqual(trackrange.decelerate, True)
    self.assertEqual(trackrange.parameter, 100)

    trackrange = IntTrackBarRanges.deserialize("-100,100,97,100")
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100)
    self.assertEqual(trackrange.values[1], 100)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, True)
    self.assertEqual(trackrange.decelerate, True)
    self.assertEqual(trackrange.parameter, 100)

    #single value

    trackrange = IntTrackBarRanges.deserialize("-100")
    self.assertEqual(len(trackrange.values), 1)
    self.assertEqual(trackrange.values[0], -100)
    self.assertEqual(trackrange.trackbartype, TrackBarType.NONE)
    self.assertEqual(trackrange.accelerate, False)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, None)

  def test_serialize (self):

    #single value without parameter

    trackrange = IntTrackBarRanges(-100)
    self.assertEqual(len(trackrange.values), 1)
    self.assertEqual(trackrange.values[0], -100)
    self.assertEqual(trackrange.trackbartype, TrackBarType.NONE)
    self.assertEqual(trackrange.accelerate, False)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, None)
    self.assertEqual(trackrange.serialize(), "-100")
    trackrangeat = trackrange.value_at(0)
    self.assertIsInstance(trackrangeat, IntTrackBarRange)
    self.assertEqual(trackrangeat.start, -100)
    self.assertEqual(trackrangeat.end, -100)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.NONE)
    self.assertEqual(trackrangeat.accelerate, False)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "-100")
    trackrangeat = trackrange.value_at(1) #if overflow, return .value_at(max).
    self.assertIsInstance(trackrangeat, IntTrackBarRange)
    self.assertEqual(trackrangeat.start, -100)
    self.assertEqual(trackrangeat.end, -100)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.NONE)
    self.assertEqual(trackrangeat.accelerate, False)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "-100")

    #2 values without parameter

    trackrange = IntTrackBarRanges((-100, 100), TrackBarType.LINEAR)
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100)
    self.assertEqual(trackrange.values[1], 100)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, False)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, None)
    self.assertEqual(trackrange.serialize(), "-100,100,1")
    trackrangeat = trackrange.value_at(0)
    self.assertIsInstance(trackrangeat, IntTrackBarRange)
    self.assertEqual(trackrangeat.start, -100)
    self.assertEqual(trackrangeat.end, 100)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, False)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "-100,100,1")
    trackrangeat = trackrange.value_at(1) #if overflow, return .value_at(max).
    self.assertIsInstance(trackrangeat, IntTrackBarRange)
    self.assertEqual(trackrangeat.start, 100)
    self.assertEqual(trackrangeat.end, 100)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, False)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "100,100,1")

    #2 values with parameter

    trackrange = IntTrackBarRanges((-100, 100), TrackBarType.LINEAR, accelerate=True)
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100)
    self.assertEqual(trackrange.values[1], 100)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, True)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, None)
    self.assertEqual(trackrange.serialize(), "-100,100,65")
    trackrangeat = trackrange.value_at(0)
    self.assertIsInstance(trackrangeat, IntTrackBarRange)
    self.assertEqual(trackrangeat.start, -100)
    self.assertEqual(trackrangeat.end, 100)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, True)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "-100,100,65")
    trackrangeat = trackrange.value_at(1) #if overflow, return .value_at(max).
    self.assertIsInstance(trackrangeat, IntTrackBarRange)
    self.assertEqual(trackrangeat.start, 100)
    self.assertEqual(trackrangeat.end, 100)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, True)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "100,100,65")

    trackrange = IntTrackBarRanges((-100, 100), TrackBarType.LINEAR, accelerate=True, parameter=100)
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100)
    self.assertEqual(trackrange.values[1], 100)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, True)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, 100)
    self.assertEqual(trackrange.serialize(), "-100,100,65,100")
    trackrangeat = trackrange.value_at(0)
    self.assertIsInstance(trackrangeat, IntTrackBarRange)
    self.assertEqual(trackrangeat.start, -100)
    self.assertEqual(trackrangeat.end, 100)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, True)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, 100)
    self.assertEqual(trackrangeat.serialize(), "-100,100,65,100")
    trackrangeat = trackrange.value_at(1) #if overflow, return .value_at(max).
    self.assertIsInstance(trackrangeat, IntTrackBarRange)
    self.assertEqual(trackrangeat.start, 100)
    self.assertEqual(trackrangeat.end, 100)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, True)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, 100)
    self.assertEqual(trackrangeat.serialize(), "100,100,65,100")

    #3 values without parameter

    trackrange = IntTrackBarRanges((-100, 100, -100), TrackBarType.LINEAR)
    self.assertEqual(len(trackrange.values), 3)
    self.assertEqual(trackrange.values[0], -100)
    self.assertEqual(trackrange.values[1], 100)
    self.assertEqual(trackrange.values[2], -100)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, False)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, None)
    self.assertEqual(trackrange.serialize(), "-100,100,1") #.serialize() always serialize first serializable-value.
    trackrangeat = trackrange.value_at(0)
    self.assertIsInstance(trackrangeat, IntTrackBarRange)
    self.assertEqual(trackrangeat.start, -100)
    self.assertEqual(trackrangeat.end, 100)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, False)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "-100,100,1")
    trackrangeat = trackrange.value_at(1)
    self.assertIsInstance(trackrangeat, IntTrackBarRange)
    self.assertEqual(trackrangeat.start, 100)
    self.assertEqual(trackrangeat.end, -100)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, False)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "100,-100,1")
    trackrangeat = trackrange.value_at(2) #if overflow, return .value_at(max).
    self.assertIsInstance(trackrangeat, IntTrackBarRange)
    self.assertEqual(trackrangeat.start, -100)
    self.assertEqual(trackrangeat.end, -100)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, False)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "-100,-100,1")

    #3 values with parameter

    trackrange = IntTrackBarRanges((-100, 100, -100), TrackBarType.LINEAR, accelerate=True)
    self.assertEqual(len(trackrange.values), 3)
    self.assertEqual(trackrange.values[0], -100)
    self.assertEqual(trackrange.values[1], 100)
    self.assertEqual(trackrange.values[2], -100)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, True)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, None)
    self.assertEqual(trackrange.serialize(), "-100,100,65") #.serialize() always serialize first serializable-value.
    trackrangeat = trackrange.value_at(0)
    self.assertIsInstance(trackrangeat, IntTrackBarRange)
    self.assertEqual(trackrangeat.start, -100)
    self.assertEqual(trackrangeat.end, 100)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, True)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "-100,100,65")
    trackrangeat = trackrange.value_at(1)
    self.assertIsInstance(trackrangeat, IntTrackBarRange)
    self.assertEqual(trackrangeat.start, 100)
    self.assertEqual(trackrangeat.end, -100)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, True)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "100,-100,65")
    trackrangeat = trackrange.value_at(2) #if overflow, return .value_at(max).
    self.assertIsInstance(trackrangeat, IntTrackBarRange)
    self.assertEqual(trackrangeat.start, -100)
    self.assertEqual(trackrangeat.end, -100)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, True)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "-100,-100,65")

    trackrange = IntTrackBarRanges((-100, 100, -100), TrackBarType.LINEAR, accelerate=True, parameter=100)
    self.assertEqual(len(trackrange.values), 3)
    self.assertEqual(trackrange.values[0], -100)
    self.assertEqual(trackrange.values[1], 100)
    self.assertEqual(trackrange.values[2], -100)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, True)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, 100)
    self.assertEqual(trackrange.serialize(), "-100,100,65,100") #.serialize() always serialize first serializable-value.
    trackrangeat = trackrange.value_at(0)
    self.assertIsInstance(trackrangeat, IntTrackBarRange)
    self.assertEqual(trackrangeat.start, -100)
    self.assertEqual(trackrangeat.end, 100)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, True)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, 100)
    self.assertEqual(trackrangeat.serialize(), "-100,100,65,100")
    trackrangeat = trackrange.value_at(1)
    self.assertIsInstance(trackrangeat, IntTrackBarRange)
    self.assertEqual(trackrangeat.start, 100)
    self.assertEqual(trackrangeat.end, -100)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, True)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, 100)
    self.assertEqual(trackrangeat.serialize(), "100,-100,65,100")
    trackrangeat = trackrange.value_at(2) #if overflow, return .value_at(max).
    self.assertIsInstance(trackrangeat, IntTrackBarRange)
    self.assertEqual(trackrangeat.start, -100)
    self.assertEqual(trackrangeat.end, -100)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, True)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, 100)
    self.assertEqual(trackrangeat.serialize(), "-100,-100,65,100")

  def test_merge (self):

    #merge single values 

    trackrange = IntTrackBarRanges(-100)
    trackrange2 = IntTrackBarRanges(-100)
    trackrangemerged = trackrange.merge(trackrange2)
    self.assertEqual(len(trackrangemerged.values), 1)
    self.assertEqual(trackrangemerged.values[0], -100)
    self.assertEqual(trackrangemerged.trackbartype, TrackBarType.NONE)
    self.assertEqual(trackrangemerged.accelerate, False)
    self.assertEqual(trackrangemerged.decelerate, False)
    self.assertEqual(trackrangemerged.parameter, None)

    #merge 2 values without parameter

    trackrange = IntTrackBarRanges((-100, 100), TrackBarType.LINEAR)
    trackrange2 = IntTrackBarRanges((100, -100), TrackBarType.LINEAR)
    trackrangemerged = trackrange.merge(trackrange2)
    self.assertEqual(len(trackrangemerged.values), 3)
    self.assertEqual(trackrangemerged.values[0], -100)
    self.assertEqual(trackrangemerged.values[1], 100)
    self.assertEqual(trackrangemerged.values[2], -100)
    self.assertEqual(trackrangemerged.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangemerged.accelerate, False)
    self.assertEqual(trackrangemerged.decelerate, False)
    self.assertEqual(trackrangemerged.parameter, None)

    #merge 2 values with parameter

    trackrange = IntTrackBarRanges((-100, 100), TrackBarType.LINEAR, accelerate=True)
    trackrange2 = IntTrackBarRanges((100, -100), TrackBarType.LINEAR, accelerate=True)
    trackrangemerged = trackrange.merge(trackrange2)
    self.assertEqual(len(trackrangemerged.values), 3)
    self.assertEqual(trackrangemerged.values[0], -100)
    self.assertEqual(trackrangemerged.values[1], 100)
    self.assertEqual(trackrangemerged.values[2], -100)
    self.assertEqual(trackrangemerged.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangemerged.accelerate, True)
    self.assertEqual(trackrangemerged.decelerate, False)
    self.assertEqual(trackrangemerged.parameter, None)

    trackrange = IntTrackBarRanges((-100, 100), TrackBarType.LINEAR, accelerate=True, parameter=100)
    trackrange2 = IntTrackBarRanges((100, -100), TrackBarType.LINEAR, accelerate=True, parameter=100)
    trackrangemerged = trackrange.merge(trackrange2)
    self.assertEqual(len(trackrangemerged.values), 3)
    self.assertEqual(trackrangemerged.values[0], -100)
    self.assertEqual(trackrangemerged.values[1], 100)
    self.assertEqual(trackrangemerged.values[2], -100)
    self.assertEqual(trackrangemerged.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangemerged.accelerate, True)
    self.assertEqual(trackrangemerged.decelerate, False)
    self.assertEqual(trackrangemerged.parameter, 100)

  def test_merge_error (self):

    #merge single values 

    trackrange = IntTrackBarRanges(100)
    trackrange2 = IntTrackBarRanges(-100)
    with self.assertRaises(ValueError):
      trackrange.merge(trackrange2)

    #merge 2 values without parameter

    trackrange = IntTrackBarRanges((100, -100), TrackBarType.LINEAR)
    trackrange2 = IntTrackBarRanges((100, -100), TrackBarType.LINEAR) #non-connectable values.
    with self.assertRaises(ValueError):
      trackrange.merge(trackrange2)

    trackrange = IntTrackBarRanges((100, -100), TrackBarType.LINEAR)
    trackrange2 = IntTrackBarRanges((-100, 100), TrackBarType.ACCELERATION) #different TrackBarType.
    with self.assertRaises(ValueError):
      trackrange.merge(trackrange2)

    #merge 2 values with parameter

    trackrange = IntTrackBarRanges((100, -100), TrackBarType.LINEAR, accelerate=False)
    trackrange2 = IntTrackBarRanges((-100, 100), TrackBarType.LINEAR, accelerate=True) #different .accelerate.
    with self.assertRaises(ValueError):
      trackrange.merge(trackrange2)

    trackrange = IntTrackBarRanges((100, -100), TrackBarType.LINEAR, accelerate=True, parameter=100)
    trackrange2 = IntTrackBarRanges((-100, 100), TrackBarType.LINEAR, accelerate=True, parameter=0) #different .parameter.
    with self.assertRaises(ValueError):
      trackrange.merge(trackrange2)
