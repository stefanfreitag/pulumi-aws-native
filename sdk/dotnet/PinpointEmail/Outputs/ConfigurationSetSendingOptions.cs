// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.PinpointEmail.Outputs
{

    [OutputType]
    public sealed class ConfigurationSetSendingOptions
    {
        public readonly bool? SendingEnabled;

        [OutputConstructor]
        private ConfigurationSetSendingOptions(bool? sendingEnabled)
        {
            SendingEnabled = sendingEnabled;
        }
    }
}
