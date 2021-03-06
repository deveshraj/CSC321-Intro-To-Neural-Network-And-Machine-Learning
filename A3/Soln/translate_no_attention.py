"""Script to visualize attention maps using a pre-trained model.

    Usage: python translate_no_attention.py --load=checkpoints/no-attn/py2
"""

import argparse
import os
import pickle as pkl
import sys
import warnings

import torch

import utils

warnings.filterwarnings("ignore")

# Local imports

words = ['roomba',
         'concert',
         'hello',
         'table',
         # Add your own words here!
         # rule 1
         'team',
         'problematic',
         # rule 2
         'ink',
         'obviously',
         # rule 3
         'shy',
         'philosophical',
         # others
         'supercalifragilisticexpialidocious'
         ]


def load(opts):
    """
    Loads the encoder, decoder and the index dictionary from the given commandline options

    :param opts: the commandline options
    :return: the encoder, decoder and the index dictionary
    """
    encoder = torch.load(os.path.join(opts.load, 'encoder.pt'))
    decoder = torch.load(os.path.join(opts.load, 'decoder.pt'))
    idx_dict = pkl.load(open(os.path.join(opts.load, 'idx_dict.pkl'), 'rb'))
    return encoder, decoder, idx_dict


def create_parser():
    """
    Creates a parser for command-line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--load', type=str, default='checkpoints/no-attn/py2',
                        help='Path to checkpoint directory.')
    parser.add_argument('--cuda', action='store_true', default=False, help='Use GPU.')
    return parser


if __name__ == '__main__':

    parser = create_parser()
    opts = parser.parse_args()

    if sys.version_info[0] == 3:
        opts.load = 'checkpoints/no-attn/py3'

    encoder, decoder, idx_dict = load(opts)

    for word in words:
        translated = utils.translate(word, encoder, decoder, idx_dict, opts)
        print('{} --> {}'.format(word, translated))
