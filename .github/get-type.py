import re
import sys

ref = sys.argv[1]

match_stable = re.match(r'refs/tags/v([0-9]+)\.([0-9]+)\.([0-9]+)', ref)
match_snapshot = re.match(r'refs/tags/snapshot-([0-9]+)', ref)
if match_stable:
	print('::set-output name=TYPE::stable')
	print('::set-output name=NAME::v%s.%s.%s' % (match_stable.group(1), match_stable.group(2), match_stable.group(3)))
elif match_snapshot:
	print('::set-output name=TYPE::snapshot')
	print('::set-output name=NAME::snapshot-%s' % match_snapshot.group(1))
else:
	print('::set-output name=TYPE::dev')
	print('::set-output name=NAME::dev')

with open('.github/mod_id.txt') as f:
	print('::set-output name=MOD_ID::' + f.read())
