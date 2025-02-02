// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Emr.Outputs
{

    [OutputType]
    public sealed class ClusterBootstrapActionConfig
    {
        public readonly string Name;
        public readonly Outputs.ClusterScriptBootstrapActionConfig ScriptBootstrapAction;

        [OutputConstructor]
        private ClusterBootstrapActionConfig(
            string name,

            Outputs.ClusterScriptBootstrapActionConfig scriptBootstrapAction)
        {
            Name = name;
            ScriptBootstrapAction = scriptBootstrapAction;
        }
    }
}
