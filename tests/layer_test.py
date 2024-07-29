import unittest

import jax
import jax.numpy as jnp
import jax.random as jrand

import equinox as eqx

import snnax.snn as snn


class TestLayer(unittest.TestCase):
    def test_simple_lif(self):
        pass

    def test_lif(self):
        pass

    def test_iaf(self):
        pass

    def test_li(self):
        key = jrand.PRNGKey(42)
        layer = snn.LI(0.95)
        shape = (16, 16)
        state, output = layer.init_state(shape, key=key)
        state += 0.5
        self.assertTrue(state.shape == shape)

        input_spikes = jrand.uniform(key, shape)
        input_spikes = jnp.where(input_spikes > 0.5, 1., 0.)
        state, output_spikes = layer(state, input_spikes)
        ground_truth = 0.475+0.05*input_spikes
        self.assertTrue(jnp.allclose(output_spikes, ground_truth))

    def test_srm(self):
        pass


if __name__ == '__main__':
    unittest.main()