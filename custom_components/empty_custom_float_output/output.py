import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import output
from esphome.const import CONF_ID

empty_custom_float_output_ns = cg.esphome_ns.namespace('empty_custom_float_output')
EmptyCustomFloatOutput = empty_custom_float_output_ns.class_('EmptyCustomFloatOutput', output.FloatOutput,
                                  cg.Component)

CONFIG_SCHEMA = output.FLOAT_OUTPUT_SCHEMA.extend({
    cv.Required(CONF_ID): cv.declare_id(EmptyCustomFloatOutput),
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield output.register_output(var, config)
    yield cg.register_component(var, config)