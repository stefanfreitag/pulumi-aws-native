// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppFlow.Inputs
{

    /// <summary>
    /// Connector specific configurations needed to create connector profile
    /// </summary>
    public sealed class ConnectorProfileConnectorProfileConfigArgs : Pulumi.ResourceArgs
    {
        [Input("connectorProfileCredentials", required: true)]
        public Input<Inputs.ConnectorProfileConnectorProfileCredentialsArgs> ConnectorProfileCredentials { get; set; } = null!;

        [Input("connectorProfileProperties")]
        public Input<Inputs.ConnectorProfileConnectorProfilePropertiesArgs>? ConnectorProfileProperties { get; set; }

        public ConnectorProfileConnectorProfileConfigArgs()
        {
        }
    }
}
