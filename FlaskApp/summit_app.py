#!C:/ProgramData/Anaconda2/python

from flask import Flask,jsonify,abort,make_response,request

from sql_connect import SQLLiteDB
from log_mgr import getLogHandler

app = Flask(__name__)

@app.route('/raise_request',methods=['POST'])
def raise_request():
    """
    This api will log the request in database
    """
    logger = getLogHandler("summit")
    logger.info("*************** Start logging for new request for raise_request method ***************")
    logger.info("Request receied with following request body")
    logger.info(request.json)
    requester = request.json['requester']
    obj = SQLLiteDB("summitqueue.db")
    request_id = obj.raise_request(requester)
    logger.info("*************** end logging for raise_request method ***************")
    return jsonify({"request_id": request_id})
    
@app.route('/request_status',methods=['POST'])
def request_status():
    """
    This api will return the request status
    """
    logger = getLogHandler("summit")
    logger.info("*************** Start logging for new request for request_status method ***************")
    logger.info("Request receied with following request body")
    logger.info(request.json)
    request_id = request.json['request_id']
    obj = SQLLiteDB("summitqueue.db")
    data = obj.get_status(request_id)
    logger.info("*************** end logging for request_status method ***************")
    return jsonify({"responce": data})
    
@app.route('/all_requests',methods=['GET'])
def all_requests():
    """
    This api will return all the requests
    """
    logger = getLogHandler("summit")
    logger.info("*************** Start logging for new request for all_requests method ***************")
    logger.info("Request receied with following request body")
    logger.info(request.json)
    obj = SQLLiteDB("summitqueue.db")
    data = obj.all_requests()
    logger.info("*************** end logging for all_requests method ***************")
    return jsonify({"responce": data})

@app.route('/pending_requests',methods=['GET'])
def pending_requests():
    """
    This api will return all pending requests
    """
    logger = getLogHandler("summit")
    logger.info("*************** Start logging for new request for pending_requests method ***************")
    logger.info("Request receied with following request body")
    logger.info(request.json)
    obj = SQLLiteDB("summitqueue.db")
    data = obj.pending_requests()
    logger.info("*************** end logging for pending_requests method ***************")
    return jsonify({"responce": data})
    
@app.route('/delete_request',methods=['POST'])
def delete_request():
    """
    This api will delete given request
    """
    logger = getLogHandler("summit")
    logger.info("*************** Start logging for new request for delete_request method ***************")
    logger.info("Request receied with following request body")
    logger.info(request.json)
    request_id = request.json['request_id']
    obj = SQLLiteDB("summitqueue.db")
    data = obj.delete_request(request_id)
    logger.info("*************** end logging for delete_request method ***************")
    return jsonify({"responce": data})

if __name__ == "__main__":
    app.run(threaded=True,debug=True,host='0.0.0.0',port=8080)