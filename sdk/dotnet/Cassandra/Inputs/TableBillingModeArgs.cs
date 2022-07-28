// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Cassandra.Inputs
{

    public sealed class TableBillingModeArgs : global::Pulumi.ResourceArgs
    {
        [Input("mode", required: true)]
        public Input<Pulumi.AwsNative.Cassandra.TableMode> Mode { get; set; } = null!;

        [Input("provisionedThroughput")]
        public Input<Inputs.TableProvisionedThroughputArgs>? ProvisionedThroughput { get; set; }

        public TableBillingModeArgs()
        {
        }
        public static new TableBillingModeArgs Empty => new TableBillingModeArgs();
    }
}
