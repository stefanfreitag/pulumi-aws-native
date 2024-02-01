// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DynamoDb.Inputs
{

    public sealed class GlobalTableKinesisStreamSpecificationArgs : global::Pulumi.ResourceArgs
    {
        [Input("approximateCreationDateTimePrecision")]
        public Input<Pulumi.AwsNative.DynamoDb.GlobalTableKinesisStreamSpecificationApproximateCreationDateTimePrecision>? ApproximateCreationDateTimePrecision { get; set; }

        [Input("streamArn", required: true)]
        public Input<string> StreamArn { get; set; } = null!;

        public GlobalTableKinesisStreamSpecificationArgs()
        {
        }
        public static new GlobalTableKinesisStreamSpecificationArgs Empty => new GlobalTableKinesisStreamSpecificationArgs();
    }
}
