remove-match-publikacji-dane:
	cd src/import_dbf && export CUSTOMER=foo && make disable-trigger
	python src/manage.py pbn_integrator --clear-match-publications
	cd src/import_dbf && export CUSTOMER=foo && make enable-trigger

remove-pbn-integracja-publikacji-dane:
	cd src/import_dbf && export CUSTOMER=foo && make disable-trigger
	python src/manage.py pbn_integrator --clear-publications
	cd src/import_dbf && export CUSTOMER=foo && make enable-trigger

remove-pbn-data:
	cd src/import_dbf && export CUSTOMER=foo && make disable-trigger
	python src/manage.py pbn_integrator --clear-all
	rm -rf pbn_json_data
	cd src/import_dbf && export CUSTOMER=foo && make enable-trigger

