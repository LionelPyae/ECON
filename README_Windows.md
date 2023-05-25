## Dependencies and Installation

- Use [Anaconda](https://www.anaconda.com/products/distribution)
- NVIDIA GPU + [CUDA](https://developer.nvidia.com/cuda-downloads)
- [Wget for Windows](https://eternallybored.org/misc/wget/1.21.3/64/wget.exe)
- Create a new folder on your C drive and rename it "wget" and move the downloaded "wget.exe" over there.
- Add the path to your wget folder to your system environment variables at `Environment Variables > System Variables Path > Edit environment variable`

![image](https://user-images.githubusercontent.com/34035011/210986038-39dbb7a1-12ef-4be9-9af4-5f658c6beb65.png)

- Install [Git for Windows 64-bit](https://git-scm.com/download/win)
- [Visual Studio Community 2022](https://visualstudio.microsoft.com/) (Make sure to check all the boxes as shown in the image below)

![image](https://user-images.githubusercontent.com/34035011/210983023-4e5a0024-68f0-4adb-8089-6ff598aec220.PNG)



## Getting started

Start by cloning the repo:

```bash
git clone https://github.com/yuliangxiu/ECON.git
cd ECON
```

## Environment

- Windows 10 / 11
- **CUDA=11.3**
- Python = 3.8
- PyTorch >= 1.12.1 (official [Get Started](https://pytorch.org/get-started/locally/))
- Cupy >= 11.3.0 (offcial [Installation](https://docs.cupy.dev/en/stable/install.html#installing-cupy-from-pypi))
- PyTorch3D = 0.7.1 (official [INSTALL.md](https://github.com/facebookresearch/pytorch3d/blob/main/INSTALL.md), recommend [install-from-local-clone](https://github.com/facebookresearch/pytorch3d/blob/main/INSTALL.md#2-install-from-a-local-clone))


```bash
# install required packages
cd ECON
conda env create -f required_env.yaml
conda activate econ
pip install cupy-cuda11x

%comspec% /k "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvars64.bat"

git clone https://github.com/facebookresearch/pytorch3d.git
cd pytorch3d
python setup.py install
set DISTUTILS_USE_SDK=1
python setup.py install
pip install cython
# install libmesh & libvoxelize
cd lib/common/libmesh
python setup.py build_ext --inplace
cd ../libvoxelize
python setup.py build_ext --inplace
```

## Register at [ICON's website](https://icon.is.tue.mpg.de/)

![Register](../assets/register.png)
Required:

- [SMPL](http://smpl.is.tue.mpg.de/): SMPL Model (Male, Female)
- [SMPL-X](http://smpl-x.is.tue.mpg.de/): SMPL-X Model, used for training
- [SMPLIFY](http://smplify.is.tue.mpg.de/): SMPL Model (Neutral)
- [PIXIE](https://icon.is.tue.mpg.de/user.php): PIXIE SMPL-X estimator

:warning: Click **Register now** on all dependencies, then you can download them all with **ONE** account.

## Downloading required models and extra data (make sure to install git and wget for windows for this to work)

```bash
cd ECON
bash fetch_data.sh # requires username and password
```

Run Command 

```bash
# For single-person image-based reconstruction (w/ l visualization steps, 1.8min)
python -m apps.inferencing -cfg ./configs/econ.yaml -in_dir ./examples -out_dir ./results
```

