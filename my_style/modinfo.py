#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from sims4communitylib.mod_support.common_mod_info import CommonModInfo


class ModInfo(CommonModInfo):
    _FILE_PATH: str = str(__file__)

    @property
    def _name(self) -> str:
        return 'MyStyle'

    @property
    def _author(self) -> str:
        return 'o19'

    @property
    def _base_namespace(self) -> str:
        return 'my_style'

    @property
    def _file_path(self) -> str:
        return ModInfo._FILE_PATH

    @property
    def _version(self) -> str:
        return '1.0.3'


r"""
# Fix 'no special outfit' Exceptions
v1.0.3
    * Added 'My Style' STBL (which is also in EP12 For Rent). >> 'My Style' will no longer be localized but display for everyone.
    * Use v1.0.2 if you have 'For Rent' and want to see a localized string.
v1.0.2
    * Change the group ID for the interaction to 0 (from 56 For Rent)
v1.0.1
    * Document 'no special outfit' behaviour (exception thrown)
v1.0.0
    * Initial version
"""