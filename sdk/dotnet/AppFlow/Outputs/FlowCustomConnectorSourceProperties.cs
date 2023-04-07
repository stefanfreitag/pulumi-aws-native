// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppFlow.Outputs
{

    [OutputType]
    public sealed class FlowCustomConnectorSourceProperties
    {
        public readonly Outputs.FlowCustomProperties? CustomProperties;
        public readonly string EntityName;

        [OutputConstructor]
        private FlowCustomConnectorSourceProperties(
            Outputs.FlowCustomProperties? customProperties,

            string entityName)
        {
            CustomProperties = customProperties;
            EntityName = entityName;
        }
    }
}
