#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2026 https://github.com/Oops19
#

from my_style.modinfo import ModInfo

from typing import Tuple, Union, Dict

import sims4.commands
import sims4.resources
from sims.outfits.outfit_enums import OutfitCategory, SpecialOutfitIndex
from sims.sim_info import SimInfo

from sims4communitylib.dialogs.common_choice_outcome import CommonChoiceOutcome
from sims4communitylib.dialogs.common_choose_outfit_dialog import CommonChooseOutfitDialog
from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand, CommonConsoleCommandArgument
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from sims4communitylib.utils.cas.common_outfit_utils import CommonOutfitUtils
from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog
from sims4communitylib.utils.localization.common_localization_utils import CommonLocalizationUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'SpecialOutfit')
log.enable()
log.debug(f"Outfits: All, Bathing (0-1), Situation (0-1), 'Career' (0-3), Special (0-3: Default, Towel, Fashion), Batuu, 'Small Business' (0-3)")

class SpecialOutfit:

    def __init__(self):
        self.outfit_list = (
                (OutfitCategory.BATHING, 0),
                (OutfitCategory.SITUATION, 0),
                (OutfitCategory.CAREER, 0), (OutfitCategory.CAREER, 1), (OutfitCategory.CAREER, 2),
                (OutfitCategory.SPECIAL, SpecialOutfitIndex.DEFAULT), (OutfitCategory.SPECIAL, SpecialOutfitIndex.TOWEL), (OutfitCategory.SPECIAL, SpecialOutfitIndex.FASHION),
                (OutfitCategory.BATUU, 0), (OutfitCategory.BATUU, 1), (OutfitCategory.BATUU, 2), (OutfitCategory.BATUU, 3), (OutfitCategory.BATUU, 4),
                (OutfitCategory.SMALL_BUSINESS, 0), (OutfitCategory.SMALL_BUSINESS, 1), (OutfitCategory.SMALL_BUSINESS, 2),
            )


    @staticmethod
    @CommonConsoleCommand(
        ModInfo.get_identity(), 'o19.my_style', 'Open the special outfit picker',
        command_arguments=(
                CommonConsoleCommandArgument('sim_id_str', 'str', 'A buff name', is_optional=True, default_value=0),
        )
    )
    def o19_cheat_my_style(output: CommonConsoleCommandOutput, sim_id_str: str = '0'):
        try:
            sim_id = int(sim_id_str)
            sim_info = CommonSimUtils.get_sim_info(sim_id)
            if sim_info:
                so = SpecialOutfit()
                so.open_outfit_picker(sim_info, so.outfit_list, None)
        except Exception as e:
            output(f"Oops: {e}")

    def open_outfit_picker(self, sim_info: SimInfo, outfit_list: Union[None, Tuple[OutfitCategory, int]] = None, exclude_outfit_categories: Union[None, Tuple[OutfitCategory]] = None):
        log.debug(f"open_outfit_picker({sim_info}, ...)")

        def _on_chosen(choice: Tuple[OutfitCategory, int], outcome: CommonChoiceOutcome):
            if outcome == CommonChoiceOutcome.CHOICE_MADE:
                CommonOutfitUtils.set_current_outfit(sim_info, choice)
                log.debug(f"Changed outfit into '{choice}'")

        try:
            dialog = CommonChooseOutfitDialog(
                ModInfo.get_identity(),
                CommonLocalizationUtils.create_localized_string(0xFC089996, tokens=(f"{sim_info.full_name}", ), localize_tokens=False),
                CommonLocalizationUtils.create_localized_string(0xFC089996, tokens=(f"My Style", ), localize_tokens=False),
            )

            if outfit_list:
                try:
                    dialog.show(sim_info, outfit_list=outfit_list, exclude_outfit_categories=exclude_outfit_categories, on_chosen=_on_chosen)
                except Exception as e:
                    log.warn(f"It seems that no outfits are available. ({e})")
            else:
                dialog.show(sim_info, on_chosen=_on_chosen)
        except Exception as e:
            log.warn(f"It seems that no outfits are available. ({e})")
        log.debug(f"Dialog closed.")
