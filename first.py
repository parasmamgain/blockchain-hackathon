#!/usr/bin/python3
from flask import Flask
from flask import *
from frames.department import Department
from sawtooth_signing.secp256k1_signer import generate_privkey
import cbor
from sawtooth_sdk.client.encoding import TransactionEncoder
from sawtooth_sdk.client.encoding import BatchEncoder
import urllib.request
from urllib.error import HTTPError

app = Flask(__name__,
	static_url_path='', 
    static_folder='static',
    template_folder='templates')

# , methods=['GET', 'POST']
@app.route('/')
def index():
	forest_dept = {
		'name': "Forst Dept",
		'id': '12',
		'link_from': '',
		'link_to': ''
	}
	# processes = Department(forest_dept)
	# processes.updateDatato(88888)
	# return some.getData("1234") + str(some.getDataFrom())


	## Try the hyper ledger things on load 
	## creating the private key	
	private_key = privkey = generate_privkey(privkey_format='bytes')

	## creating the encoder using the private_key
	encoder = TransactionEncoder(
	    private_key,
	    # We don't want a batcher pubkey or dependencies for our example,
	    # but this is what setting them might look like:
	    # batcherPubkey='02d260a46457a064733153e09840c322bee1dff34445d7d49e19e60abd18fd0758',
	    # dependencies=['540a6803971d1880ec73a96cb97815a95d374cbad5d865925e5aa0432fcf1931539afe10310c122c5eaae15df61236079abbf4f258889359c4d175516934484a'],
	    payload_encoder=cbor.dumps,
	    family_name='intkey',
	    family_version='1.0',
	    inputs=['1cf1266e282c41be5e4254d8820772c5518a2c5a8c0c7f7eda19594a7eb539453e1ed7'],
	    outputs=['1cf1266e282c41be5e4254d8820772c5518a2c5a8c0c7f7eda19594a7eb539453e1ed7'],
	    payload_encoding='application/cbor')

	## create the txn packet
	txn = encoder.create({
	    'Verb': 'Running',
	    'Name': 'Amar',
	    'Value': 1})

	## we could be encoding this further .. if the same was being used to update into a chain .. over some other network

	## We need to create the BatchEncoder to create the batches
	batcher = BatchEncoder(private_key)

	## create the batch 
	batch = batcher.create(txn)
	print(' the batch is ')

	## just like the txn encoder .. the batch encoder can also be serialized if being sent over a network .. 
	## but we skip it for now
	#batch_bytes = batcher.encode([batch, batch2, batch3])

	batch_bytes = batcher.create_encoded(txn)

	output = open('intkey.batches', 'wb')
	output.write(batch_bytes)


	## submitting the batches to the validator
	try:
	    request = urllib.request.Request(
	        'http://localhost:8080/batches',
	        batch_bytes,
	        method='POST',
	        headers={'Content-Type': 'application/octet-stream'})
	    response = urllib.request.urlopen(request)

	except HTTPError as e:
	    response = e.file

	print(' this is the end of the network interaction - - ')

	return render_template('index.html')

@app.route('/list_request')
def list_request():
    return render_template('list_requests.html')


if __name__ == '__main__':
    app.run(debug=True)




# on start, spawn dashboard.
