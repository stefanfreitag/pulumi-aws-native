// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Greengrass.Inputs
{

    public sealed class ConnectorDefinitionConnectorArgs : global::Pulumi.ResourceArgs
    {
        [Input("connectorArn", required: true)]
        public Input<string> ConnectorArn { get; set; } = null!;

        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        [Input("parameters")]
        public Input<object>? Parameters { get; set; }

        public ConnectorDefinitionConnectorArgs()
        {
        }
        public static new ConnectorDefinitionConnectorArgs Empty => new ConnectorDefinitionConnectorArgs();
    }
}
