# allianceauth-blacklist

**You Shall Not Pass!**

## Installation

1. Install from pip `pip install git+https://github.com/Solar-Helix-Independent-Transport/allianceauth-blacklist.git`
2. Add `'blacklist'` to INSTALLED_APPS in local.py
3. Run the management command to update AA's State system `python myauth/manage.py blacklist_state`
4. Give permissions
5. done ski

## Features

- Integration with Alliance Auth's State System, creates an maintains a Blacklisted State to ensure no services access is granted to Blacklisted users
- Notes
- Comments on Notes

## Permissions

Perm | Admin Site | Auth Site
 --- | --- | ---

view_basic_eve_notes | Can View own corps notes
view_eve_blacklist | Can View the Blacklist
add_to_blacklist | Can add to Blacklist

view_eve_notes | Can view all eve notes
add_basic_eve_notes | Can Add own corp members to notes
add_new_eve_notes | Can add new eve notes
view_restricted_eve_notes | Can View restricted eve notes
add_restricted_eve_notes | Can Add restricted eve notes

view_eve_note_comments | Can view eve note comments
view_eve_note_restricted_comments | Can view restricted eve note comments
add_new_eve_note_comments | Can add comments on eve notes
add_new_eve_note_restricted_comments | Can add new restricted comments to eve notes

## Contributing

Make sure you have signed the [License Agreement](https://developers.eveonline.com/resource/license-agreement) by logging in at <https://developers.eveonline.com> before submitting any pull requests. All bug fixes or features must not include extra superfluous formatting changes.
