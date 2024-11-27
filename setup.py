# Copyright 2024 ByteDance and/or its affiliates.
#
# Licensed under the Attribution-NonCommercial 4.0 International
# License (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the
# License at

#     https://creativecommons.org/licenses/by-nc/4.0/

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name="protenix",
    python_requires='>=3.10',
    version="0.0.1",
    description="A trainable PyTorch reproduction of AlphaFold 3.",
    author="Bytedance AML AI4S Team",
    author_email="ai4s-bio@bytedance.com",
    packages=find_packages(
        exclude=(
            "assets",
            "benchmark",
            "*.egg-info",
        )
    ),
    include_package_data=True,
    package_data={
        "protenix": ["model/layer_norm/kernel/*"],
    },
    install_requires=install_requires,
    license="Attribution-NonCommercial 4.0 International License",
    entry_points={
        "console_scripts": [
            "protenix_infer = runner.inference:run_default",
        ],
    }
)
