// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Kendra.Inputs
{

    public sealed class DataSourceConnectionConfigurationArgs : Pulumi.ResourceArgs
    {
        [Input("databaseHost", required: true)]
        public Input<string> DatabaseHost { get; set; } = null!;

        [Input("databaseName", required: true)]
        public Input<string> DatabaseName { get; set; } = null!;

        [Input("databasePort", required: true)]
        public Input<int> DatabasePort { get; set; } = null!;

        [Input("secretArn", required: true)]
        public Input<string> SecretArn { get; set; } = null!;

        [Input("tableName", required: true)]
        public Input<string> TableName { get; set; } = null!;

        public DataSourceConnectionConfigurationArgs()
        {
        }
    }
}
