# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import subprocess
from libqtile import hook
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import backlight

def mygroupwidget(wid,orientation, color):
    # if orientation=="up":
    #     return (
    #         widget.TextBox(text="", fontsize="27", foreground=color, padding=-2),
    #         wid,           
    #         widget.TextBox(text="", fontsize="27", foreground=color, padding=-2)
    #             )
    # elif orientation=="down":
    #     return (
    #         widget.TextBox(text="", fontsize="27", foreground=colorv2, padding=-2),
    #         wid,
    #         widget.TextBox(text="", fontsize="27", foreground=colorv2, padding=-2)
    #     )
    return (wid)

mod = "mod4"
terminal = "alacritty"
web_browser = "firefox"
editor = "code"
explorer = "thunar"
blue = "#366cc2"
ars = "#366"


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "j", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "i", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "j", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "i", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "j", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "k", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "i", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    
    # Captura de pantalla
    Key([], "Print", lazy.spawn("scrot /home/juanecos/Imágenes/Screenshots/screenshot_%Y-%m-%d_%H-%M-%S.png"), desc="Captura toda la pantalla"),
    Key([mod, "Shift"], "s", lazy.spawn("scrot -s /home/juanecos/Imágenes/Screenshots/screenshot_%Y-%m-%d_%H-%M-%S.png"), desc="Captura seleccion"),
    Key([mod, "Control"], "Print", lazy.spawn("scrot -u /home/juanecos/Imágenes/Screenshots/screenshot_%Y-%m-%d_%H-%M-%S.png"), desc="Captura seleccion"),
    
    # scrot -u para la ventana  actual
    #como hacerlo al portapapeles?
    #quiero subirlelacalidadi} tambien
    #
    
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(f'{terminal} --config-file="/home/juanecos/.config/alacritty/alacritty.conf"'), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "r", lazy.spawn("qtile cmd-obj -o cmd -f restart"), desc="Restart Qtile"),
    
   
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    # Menu de rofi
    Key([mod], "m", lazy.spawn("bash /home/juanecos/.config/rofi/launchers/type-2/launcher.sh"), desc="Rofi menu"),
    Key([mod], "Menu", lazy.spawn("bash /home/juanecos/.config/rofi/launchers/type-2/launcher.sh"), desc="Rofi menu"),
    
    # Menu de apagado 
    Key([mod, "control"], "delete", lazy.spawn("bash /home/juanecos/.config/rofi/powermenu/type-1/powermenu.sh"), desc="Rofi menu"),
    
    # Teclas personalizadas

    # Abrir thunar
    Key([mod], "e", lazy.spawn(explorer), desc="Open en thunar"),
    # Abrir firefox
    Key([mod], "w", lazy.spawn(web_browser), desc="Open firefox"),
    # Visual Studio Code
    Key([mod], "c", lazy.spawn(editor), desc="Open Code"),

    # Subir y bajar el brillo
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 1"), desc="Lower Brightness by 5%"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 1"), desc="Raise Brightness by 5%"),

    Key([mod], "left", lazy.spawn("xbacklight -dec 1"), desc="Lower Brightness by 5%"),
    Key([mod], "right", lazy.spawn("xbacklight -inc 1"), desc="Raise Brightness by 5%"),

    # Sound
    Key([], "XF86AudioMute", lazy.spawn("pamixer -t")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer -d 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer -i 5")),

    Key([mod], "Down", lazy.spawn("pamixer -d 5")),
    Key([mod], "Up", lazy.spawn("pamixer -i 5")),

    
]
# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

#defino el label que tendran los escritorios
desk = ["󰣇","󰈹","","󰨞","","󰝚","󰡨"]


"""
listado de nerdfonts
1 nf-md-arch 
2 nf-md-firefox
3 nf-dev-terminal
4 nf-md-microsoft_visual_studio_code
5 nf-fa-folder_open
6 nf-fa-music
7 nf-fa-docker
"""


#inicializo un array donde quedaran almacendos los objetos Group
#groups= [Group(i) for i in "12345678"]
groups = []

# #relleno la informacin de cada grupo  iterando el array principal
# for i in range(0, len(desk)):
#     # label se usa para darle nombre
#     team = Group(str(i+1), label=desk[i])
#     groups.append(team)

for idx, label in enumerate(desk):
    team = Group(str(idx + 1), label=label)
    groups.append(team)

#Define los nombres de las teclas del teclado numérico
keypad_mapping = {
    "1": "KP_End",
    "2": "KP_Down",
    "3": "KP_Next",
    "4": "KP_Left",
    "5": "KP_Begin",
    "6": "KP_Right",
    "7": "KP_Home",
    "8": "KP_Up",
    "9": "KP_Prior",
}

for i in groups:
    alias= f"KP_{i.name}"
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            Key(
                [mod],
                keypad_mapping[i.name],  # Usa el mapeo para teclas del teclado numérico
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name} (keypad)",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            Key(
                [mod, "shift"],
                keypad_mapping[i.name],  # Usa el mapeo para teclas del teclado numérico
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name} (keypad)",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
borderfocus = "#6f7ec9"
bordernormal= "#4a5a61"

layouts = [
    layout.Columns(margin=4, border_width=2, border_focus=borderfocus,border_normal=bordernormal),
    #border_focus_stack=["#ab65c9", "#61357a"]
    layout.Max(margin=0),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    #layout.Bsp(),
    layout.Matrix(margin=4, border_width=2, border_focus=borderfocus,border_normal=bordernormal),
    #layout.MonadTall(),
    #layout.MonadWide(),
    #layout.RatioTile(),
    layout.Tile(margin=4, border_width=2, border_focus=borderfocus,border_normal=bordernormal),
    layout.TreeTab(margin=4, border_width=2, border_focus=borderfocus,border_normal=bordernormal),
    layout.Floating(border_width=2, border_focus=borderfocus,border_normal=bordernormal),
    
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


# colorv1 ="#2A3335"
# colorv2= "#0A5EB0"
# colorv3 ="#0A97B0"
# colorv4 ="#FFCFEF"


colorv8="#B03A42"
colorv7="#CB923C"
colorv6="#138F8B"
colorv5="#2492C2"
colorv4="#1369A5"
colorv3="#5D3385"
colorv2="#813287"
colorv1="#1D1F29"


        
screens = [
    Screen(
        top=bar.Bar(
            [

                # widget.QuickExit(),
                widget.GroupBox(
                    
                    fontsize=30,
                    highlight_method='block',  # Opcional, para resaltar grupos activos
                    active="#ffffff",            # Color de los grupos activos
                    inactive="#9dacc4",          # Color de los grupos inactivos
                    this_current_screen_border=blue,  # Borde del grupo activo
                    padding=7,
                    ),
                
                

                widget.Sep(linewidth=0,padding=10),
                widget.WindowName(),
                widget.Chord(background=blue),
                # widget.TextBox(
                #     text="Menu",
                #     mouse_callbacks={"Button1": lazy.spawn("bash /home/juanecos/.config/rofi/launchers/type-2/launcher.sh")},
                #     fontsize=14,
                #     foreground="#fff",
                #     backgroun="#5f5f5f"
                # ),

                widget.Sep(linewidth=0,padding=10),
                # nf-ple-upper_left_triangle nf-ple-upper_right_triangle    
                # nf-ple-lower_right_triangle nf-ple-lower_left_triangle   
                
                #widget.Pomodoro(),

                
                widget.TextBox(text="", fontsize="27", foreground=colorv7, padding=-2),
                widget.CurrentLayoutIcon(background=colorv7),
                widget.CurrentLayout(background=colorv7, width=50),
                widget.TextBox(text="", fontsize="27", foreground=colorv7, padding=-2),
                
                widget.TextBox(text="", fontsize="27", foreground=colorv6, padding=-2),
                widget.TextBox(text="󱑢", fontsize="27", foreground="#fff", background=colorv6),
                widget.CheckUpdates(display_format="{updates}",background=colorv6),
                widget.TextBox(text="", fontsize="27", foreground=colorv6, padding=-2),

                widget.TextBox(text="", fontsize="27", foreground=colorv5, padding=-2),
                widget.TextBox(text="", fontsize="27", foreground="#fff", background=colorv5),
                widget.ThermalSensor(background=colorv5),
                widget.TextBox(text="", fontsize="27", foreground=colorv5, padding=-2),
                
                
                widget.TextBox(text="", fontsize="27", foreground=colorv4, padding=-2),
                #widget.CheckUpdates(display_format="{updates}"),
                widget.TextBox(text="", fontsize="27", foreground="#fff", background=colorv4),
                widget.Memory(background=colorv4, format="{MemUsed: .2f}{mm}/{MemTotal: .2f}{mm}", measure_mem="G"),
                widget.TextBox(text="", fontsize="27", foreground=colorv4, padding=-2),
                
                
                
                widget.TextBox(text="", fontsize="27", foreground=colorv3, padding=-2),
                widget.TextBox(text="", fontsize="27", foreground="#fff", background=colorv3),
                widget.CPU(background=colorv3, format="{freq_current}GHz {load_percent}%",width=80),
                widget.TextBox(text="", fontsize="27", foreground=colorv3, padding=-2),
                #mygroupwidget((widget.CurrentLayout(background=colorv3)),"down",colorv3),
                # widget.WidgetBox(widgets=[
                # widget.TextBox(text="This widget is in the box"),
               #widget.Wallpaper(directory="/home/juanecos/Imágenes/wallpaper"),
                # widget.Memory()]
                # ),
                
                            
                widget.TextBox(text="", fontsize="27", foreground=colorv2, padding=-2),
                widget.TextBox(text="", fontsize="27", foreground="#fff", background=colorv2),
                widget.Clock(format='%d/%m/%y %H:%M',background=colorv2),
                widget.TextBox(text="", fontsize="27", foreground=colorv2, padding=-2),
                
                widget.TextBox(text="", fontsize="27", foreground=colorv1, padding=-2),
                widget.Systray(background=colorv1),
                widget.Sep(linewidth=0,padding=10, background=colorv1),
                
            ],
            28,
            #background = "#5e4866"
            border_width=[0, 0, 0, 2],  # Draw top and bottom borders
            #border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
    Click([mod], "Button5", lazy.screen.next_group()),
    Click([mod], "Button4", lazy.screen.prev_group()),
    
    
    # Cambiar al grupo anterior con Mod + Rueda abajo
    # Click([mod], "Button5", lazy.screen.prev_group(), desc="Ir al grupo anterior"),
    # # Cambiar al grupo siguiente con Mod + Rueda arriba
    #Click([mod], "Button8", lazy.screen.next_group(), desc="Ir al grupo siguiente"),
    

]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("/home/juanecos/.config/qtile/autostart.sh")
    subprocess.run([script])
