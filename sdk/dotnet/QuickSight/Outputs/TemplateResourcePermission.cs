// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    [OutputType]
    public sealed class TemplateResourcePermission
    {
        public readonly ImmutableArray<string> Actions;
        public readonly string Principal;

        [OutputConstructor]
        private TemplateResourcePermission(
            ImmutableArray<string> actions,

            string principal)
        {
            Actions = actions;
            Principal = principal;
        }
    }
}
