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
    /// &lt;p&gt;Trino parameters.&lt;/p&gt;
    /// </summary>
    public sealed class DataSourceTrinoParametersArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// &lt;p&gt;Catalog.&lt;/p&gt;
        /// </summary>
        [Input("catalog", required: true)]
        public Input<string> Catalog { get; set; } = null!;

        /// <summary>
        /// &lt;p&gt;Host.&lt;/p&gt;
        /// </summary>
        [Input("host", required: true)]
        public Input<string> Host { get; set; } = null!;

        /// <summary>
        /// &lt;p&gt;Port.&lt;/p&gt;
        /// </summary>
        [Input("port", required: true)]
        public Input<double> Port { get; set; } = null!;

        public DataSourceTrinoParametersArgs()
        {
        }
        public static new DataSourceTrinoParametersArgs Empty => new DataSourceTrinoParametersArgs();
    }
}
