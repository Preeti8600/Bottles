import os
import shutil
from pathlib import Path
from ..utils import DisplayUtils


class API:
    notifications = "https://raw.githubusercontent.com/bottlesdevs/data/main/notifications.yml"
    
class Samples:

    data = {
        "notifications": []
    }

    config = {
        "Name": "",
        "Arch": "win64",
        "Windows": "win10",
        "Runner": "",
        "WorkingDir": "",
        "DXVK": "",
        "NVAPI": "",
        "VKD3D": "",
        "Path": "",
        "Custom_Path": False,
        "Environment": "",
        "Creation_Date": "",
        "Update_Date": "",
        "Versioning": False,
        "State": 0,
        "Parameters": {
            "dxvk": False,
            "dxvk_hud": False,
            "dxvk_nvapi": False,
            "vkd3d": False,
            "gamemode": False,
            "sync": "wine",
            "fsr": False,
            "fsr_level": 5,
            "aco_compiler": False,
            "discrete_gpu": False,
            "virtual_desktop": False,
            "virtual_desktop_res": "1280x720",
            "pulseaudio_latency": False,
            "fixme_logs": False,
            "environment_variables": "",
            "use_runtime": False,
        },
        "Installed_Dependencies": [],
        "DLL_Overrides": {},
        "Programs": {},
        "External_Programs": {},
        "Uninstallers": {},
        "Latest_Executables": []
    }

    environments = {
        "gaming": {
            "Runner": "wine",
            "Parameters": {
                "dxvk": True,
                # "nvapi": True,
                "vkd3d": False,
                "sync": "esync",
                "fsr": False,
                "discrete_gpu": True,
                "pulseaudio_latency": True
            },
            "Installed_Dependencies": [
                "d3dx9",
                "msls31",
                "arial32",
                "times32",
                "courie32",
                "d3dcompiler_43",
                "d3dcompiler_47"
            ]
        },
        "software": {
            "Runner": "wine",
            "Parameters": {
                "dxvk": True,
                "vkd3d": True
            },
            "Installed_Dependencies": [
                "arial32",
                "times32",
                "courie32",
                "dotnet48"
            ]
        },
        "layered": {
            "Runner": "wine",
            "Parameters": {},
            "Installed_Dependencies": []
        },
    }


class BottlesRepositories:
    components = "https://raw.githubusercontent.com/bottlesdevs/components/main/"
    components_index = f"{components}/index.yml"

    dependencies = "https://raw.githubusercontent.com/bottlesdevs/dependencies/main/"
    dependencies_index = f"{dependencies}/index.yml"

    installers = "https://raw.githubusercontent.com/bottlesdevs/programs/main/"
    installers_index = f"{installers}/index.yml"

    if "TESTING_REPOS" in os.environ and int(os.environ["TESTING_REPOS"]) == 1:
            dependencies_index = f"{dependencies}/testing.yml"
            components_index = f"{components}/testing.yml"


class Paths:

    # Icon paths
    icons_user = f"{Path.home()}/.local/share/icons"

    # Local paths
    base = f"{Path.home()}/.local/share/bottles"

    # User applications path
    applications = f"{Path.home()}/.local/share/applications/"

    if "FLATPAK_ID" in os.environ:
        base_n = base
        base = f"{Path.home()}/.var/app/{os.environ['FLATPAK_ID']}/data/bottles"

    temp = f"{base}/temp"
    runners = f"{base}/runners"
    bottles = f"{base}/bottles"
    dxvk = f"{base}/dxvk"
    vkd3d = f"{base}/vkd3d"
    nvapi = f"{base}/nvapi"
    data = f"{base}/data.yml"


class TrdyPaths:

    # External managers paths
    lutris = f"{Path.home()}*/Games"
    playonlinux = f"{Path.home()}/.PlayOnLinux/wineprefix/"
    bottlesv1 = f"{Path.home()}/.Bottles"


CMDSettings = {
    "ColorTable00":"2368548", 
    "CursorSize": "25",
    "CursorVisible": "1",
    "EditionMode": "0",
    "FaceName": "Monospace",
    "FontPitchFamily": "1",
    "FontSize":"1248584", 
    "FontWeight": "400",
    "HistoryBufferSize": "50",
    "HistoryNoDup": "0",
    "InsertMode": "1",
    "MenuMask": "0",
    "PopupColors": "245",
    "QuickEdit": "1",
    "ScreenBufferSize": "9830480",
    "ScreenColors":"11", 
    "WindowSize": "1638480"
}


# Check if gamemode is available
gamemode_available = False
if shutil.which("gamemoderun") is not None:
    gamemode_available = True

x_display = DisplayUtils.get_x_display()
