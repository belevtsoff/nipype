# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.algorithms.misc import SimpleThreshold

def test_SimpleThreshold_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    threshold=dict(mandatory=True,
    ),
    volumes=dict(mandatory=True,
    ),
    )
    inputs = SimpleThreshold.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_SimpleThreshold_outputs():
    output_map = dict(thresholded_volumes=dict(),
    )
    outputs = SimpleThreshold.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

