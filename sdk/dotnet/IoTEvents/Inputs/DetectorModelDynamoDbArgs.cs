// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTEvents.Inputs
{

    /// <summary>
    /// Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the [payload](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html). One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. For more information, see [Actions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-event-actions.html) in *AWS IoT Events Developer Guide*.
    /// </summary>
    public sealed class DetectorModelDynamoDbArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the hash key (also called the partition key).
        /// </summary>
        [Input("hashKeyField", required: true)]
        public Input<string> HashKeyField { get; set; } = null!;

        /// <summary>
        /// The data type for the hash key (also called the partition key). You can specify the following values:
        /// 
        /// * `STRING` - The hash key is a string.
        /// 
        /// * `NUMBER` - The hash key is a number.
        /// 
        /// If you don't specify `hashKeyType`, the default value is `STRING`.
        /// </summary>
        [Input("hashKeyType")]
        public Input<string>? HashKeyType { get; set; }

        /// <summary>
        /// The value of the hash key (also called the partition key).
        /// </summary>
        [Input("hashKeyValue", required: true)]
        public Input<string> HashKeyValue { get; set; } = null!;

        /// <summary>
        /// The type of operation to perform. You can specify the following values:
        /// 
        /// * `INSERT` - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key.
        /// 
        /// * `UPDATE` - Update an existing item of the DynamoDB table with new data. This item's partition key must match the specified hash key. If you specified a range key, the range key must match the item's sort key.
        /// 
        /// * `DELETE` - Delete an existing item of the DynamoDB table. This item's partition key must match the specified hash key. If you specified a range key, the range key must match the item's sort key.
        /// 
        /// If you don't specify this parameter, AWS IoT Events triggers the `INSERT` operation.
        /// </summary>
        [Input("operation")]
        public Input<string>? Operation { get; set; }

        [Input("payload")]
        public Input<Inputs.DetectorModelPayloadArgs>? Payload { get; set; }

        /// <summary>
        /// The name of the DynamoDB column that receives the action payload.
        /// 
        /// If you don't specify this parameter, the name of the DynamoDB column is `payload`.
        /// </summary>
        [Input("payloadField")]
        public Input<string>? PayloadField { get; set; }

        /// <summary>
        /// The name of the range key (also called the sort key).
        /// </summary>
        [Input("rangeKeyField")]
        public Input<string>? RangeKeyField { get; set; }

        /// <summary>
        /// The data type for the range key (also called the sort key), You can specify the following values:
        /// 
        /// * `STRING` - The range key is a string.
        /// 
        /// * `NUMBER` - The range key is number.
        /// 
        /// If you don't specify `rangeKeyField`, the default value is `STRING`.
        /// </summary>
        [Input("rangeKeyType")]
        public Input<string>? RangeKeyType { get; set; }

        /// <summary>
        /// The value of the range key (also called the sort key).
        /// </summary>
        [Input("rangeKeyValue")]
        public Input<string>? RangeKeyValue { get; set; }

        /// <summary>
        /// The name of the DynamoDB table.
        /// </summary>
        [Input("tableName", required: true)]
        public Input<string> TableName { get; set; } = null!;

        public DetectorModelDynamoDbArgs()
        {
        }
        public static new DetectorModelDynamoDbArgs Empty => new DetectorModelDynamoDbArgs();
    }
}
