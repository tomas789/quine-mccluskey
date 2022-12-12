from __future__ import annotations, print_function

import sys
from typing import Iterable, List, Optional, Set, Tuple

import quine_mccluskey_tomas789._quine_mccluskey_tomas789 as _qmc


def reduce_simple_xor_terms(t1: str, t2: str) -> Optional[str]:
    return _qmc.reduce_simple_xor_terms(t1, t2)


def reduce_simple_xnor_terms(t1: str, t2: str) -> Optional[str]:
    return _qmc.reduce_simple_xnor_terms(t1, t2)


def get_prime_implicants(n_bits: int, use_xor: bool, terms: Set[str]) -> ResultWithProfile:
    """Simplify the set 'terms'.

    Args:
        terms (set of str): set of strings representing the minterms of
        ones and dontcares.

    Returns:
        A set of prime implicants. These are the minterms that cannot be
        reduced with step 1 of the Quine McCluskey method.

    This is the very first step in the Quine McCluskey algorithm. This
    generates all prime implicants, whether they are redundant or not.
    """
    r = _qmc.get_prime_implicants(n_bits, use_xor, terms)

    return ResultWithProfile(
        result=r.result, profile_cmp=r.profile_cmp, profile_xor=r.profile_xor, profile_xnor=r.profile_xnor
    )


def get_essential_implicants(n_bits: int, terms: Set[str], dc: Set[str]) -> Set[str]:
    return _qmc.get_essential_implicants(n_bits, terms, dc)


def get_term_rank(term: str, term_range: int) -> int:
    return _qmc.get_term_rank(term, term_range)


def permutations(value: str = "", exclude: Set[str] = set()) -> Set[str]:
    return _qmc.permutations(value, exclude)


def get_terms(implicant: str) -> Tuple[List[int], List[int], List[int], List[int], List[int]]:
    return _qmc.get_terms(implicant)


def complexity(implicant: str) -> float:
    return _qmc.complexity(implicant)


def combine_implicants(a: str, b: str, dc: Set[str]) -> Optional[str]:
    return _qmc.combine_implicants(a, b, dc)


def reduce_implicants(n_bits: int, implicants: Set[str], dc: Set[str]) -> Set[str]:
    return _qmc.reduce_implicants(n_bits, implicants, dc)


def simplify_los_with_profile(
    ones: Iterable[str], dc: Iterable[str] = [], num_bits: Optional[int] = None, use_xor: bool = True
) -> ResultWithProfile:
    """Implementation for the simplify_los function."""
    return _qmc.simplify_los_with_profile(list(ones), list(dc), num_bits, use_xor)


def simplify_with_profile(
    ones: List[int], dc: List[int] = [], num_bits: Optional[int] = None, use_xor: bool = False
) -> ResultWithProfile:
    return _qmc.simplify_with_profile(ones, dc, num_bits, use_xor)


def simplify(ones: List[int], dc: List[int] = [], num_bits: Optional[int] = None, use_xor: bool = False) -> Optional[Set[str]]:
    return _qmc.simplify(ones, dc, num_bits, use_xor)


def simplify_los(
    ones: Iterable[str], dc: Iterable[str] = [], num_bits: Optional[int] = None, use_xor: bool = False
) -> Optional[Set[str]]:
    return _qmc.simplify_los(ones, dc, num_bits, use_xor)
