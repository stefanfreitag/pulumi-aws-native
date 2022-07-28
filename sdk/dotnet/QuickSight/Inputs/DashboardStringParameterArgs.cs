// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    /// <summary>
    /// &lt;p&gt;A string parameter.&lt;/p&gt;
    /// </summary>
    public sealed class DashboardStringParameterArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// &lt;p&gt;A display name for a string parameter.&lt;/p&gt;
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("values", required: true)]
        private InputList<string>? _values;

        /// <summary>
        /// &lt;p&gt;The values of a string parameter.&lt;/p&gt;
        /// </summary>
        public InputList<string> Values
        {
            get => _values ?? (_values = new InputList<string>());
            set => _values = value;
        }

        public DashboardStringParameterArgs()
        {
        }
        public static new DashboardStringParameterArgs Empty => new DashboardStringParameterArgs();
    }
}
