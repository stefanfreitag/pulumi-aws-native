// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Greengrass.Outputs
{

    [OutputType]
    public sealed class ConnectorDefinitionConnectorDefinitionVersion
    {
        public readonly ImmutableArray<Outputs.ConnectorDefinitionConnector> Connectors;

        [OutputConstructor]
        private ConnectorDefinitionConnectorDefinitionVersion(ImmutableArray<Outputs.ConnectorDefinitionConnector> connectors)
        {
            Connectors = connectors;
        }
    }
}
