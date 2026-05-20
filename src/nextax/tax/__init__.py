"""NexTax Tax Module — US federal tax calculation and filing assistance.

Provides tax constants, calculation engine, form data models,
and optimization tools for comprehensive US tax filing.
"""

from nextax.tax.calculator import TaxCalculator
from nextax.tax.forms import FilingStatus

__all__ = ["TaxCalculator", "FilingStatus"]
