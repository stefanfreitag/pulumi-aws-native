// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AmplifyUIBuilder.Inputs
{

    public sealed class ComponentVariantArgs : global::Pulumi.ResourceArgs
    {
        [Input("overrides")]
        public Input<Inputs.ComponentOverridesArgs>? Overrides { get; set; }

        [Input("variantValues")]
        public Input<Inputs.ComponentVariantValuesArgs>? VariantValues { get; set; }

        public ComponentVariantArgs()
        {
        }
        public static new ComponentVariantArgs Empty => new ComponentVariantArgs();
    }
}
