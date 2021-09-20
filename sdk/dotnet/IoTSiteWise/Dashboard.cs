// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTSiteWise
{
    /// <summary>
    /// Resource schema for AWS::IoTSiteWise::Dashboard
    /// </summary>
    [AwsNativeResourceType("aws-native:iotsitewise:Dashboard")]
    public partial class Dashboard : Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN of the dashboard.
        /// </summary>
        [Output("dashboardArn")]
        public Output<string> DashboardArn { get; private set; } = null!;

        /// <summary>
        /// The dashboard definition specified in a JSON literal.
        /// </summary>
        [Output("dashboardDefinition")]
        public Output<string> DashboardDefinition { get; private set; } = null!;

        /// <summary>
        /// A description for the dashboard.
        /// </summary>
        [Output("dashboardDescription")]
        public Output<string> DashboardDescription { get; private set; } = null!;

        /// <summary>
        /// The ID of the dashboard.
        /// </summary>
        [Output("dashboardId")]
        public Output<string> DashboardId { get; private set; } = null!;

        /// <summary>
        /// A friendly name for the dashboard.
        /// </summary>
        [Output("dashboardName")]
        public Output<string> DashboardName { get; private set; } = null!;

        /// <summary>
        /// The ID of the project in which to create the dashboard.
        /// </summary>
        [Output("projectId")]
        public Output<string?> ProjectId { get; private set; } = null!;

        /// <summary>
        /// A list of key-value pairs that contain metadata for the dashboard.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.DashboardTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Dashboard resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Dashboard(string name, DashboardArgs args, CustomResourceOptions? options = null)
            : base("aws-native:iotsitewise:Dashboard", name, args ?? new DashboardArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Dashboard(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iotsitewise:Dashboard", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Dashboard resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Dashboard Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Dashboard(name, id, options);
        }
    }

    public sealed class DashboardArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The dashboard definition specified in a JSON literal.
        /// </summary>
        [Input("dashboardDefinition", required: true)]
        public Input<string> DashboardDefinition { get; set; } = null!;

        /// <summary>
        /// A description for the dashboard.
        /// </summary>
        [Input("dashboardDescription", required: true)]
        public Input<string> DashboardDescription { get; set; } = null!;

        /// <summary>
        /// A friendly name for the dashboard.
        /// </summary>
        [Input("dashboardName", required: true)]
        public Input<string> DashboardName { get; set; } = null!;

        /// <summary>
        /// The ID of the project in which to create the dashboard.
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        [Input("tags")]
        private InputList<Inputs.DashboardTagArgs>? _tags;

        /// <summary>
        /// A list of key-value pairs that contain metadata for the dashboard.
        /// </summary>
        public InputList<Inputs.DashboardTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.DashboardTagArgs>());
            set => _tags = value;
        }

        public DashboardArgs()
        {
        }
    }
}
