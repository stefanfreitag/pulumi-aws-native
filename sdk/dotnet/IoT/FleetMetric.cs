// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT
{
    /// <summary>
    /// An aggregated metric of certain devices in your fleet
    /// </summary>
    [AwsNativeResourceType("aws-native:iot:FleetMetric")]
    public partial class FleetMetric : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The aggregation field to perform aggregation and metric emission
        /// </summary>
        [Output("aggregationField")]
        public Output<string?> AggregationField { get; private set; } = null!;

        [Output("aggregationType")]
        public Output<Outputs.FleetMetricAggregationType?> AggregationType { get; private set; } = null!;

        /// <summary>
        /// The creation date of a fleet metric
        /// </summary>
        [Output("creationDate")]
        public Output<string> CreationDate { get; private set; } = null!;

        /// <summary>
        /// The description of a fleet metric
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The index name of a fleet metric
        /// </summary>
        [Output("indexName")]
        public Output<string?> IndexName { get; private set; } = null!;

        /// <summary>
        /// The last modified date of a fleet metric
        /// </summary>
        [Output("lastModifiedDate")]
        public Output<string> LastModifiedDate { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Number (ARN) of a fleet metric metric
        /// </summary>
        [Output("metricArn")]
        public Output<string> MetricArn { get; private set; } = null!;

        /// <summary>
        /// The name of the fleet metric
        /// </summary>
        [Output("metricName")]
        public Output<string> MetricName { get; private set; } = null!;

        /// <summary>
        /// The period of metric emission in seconds
        /// </summary>
        [Output("period")]
        public Output<int?> Period { get; private set; } = null!;

        /// <summary>
        /// The Fleet Indexing query used by a fleet metric
        /// </summary>
        [Output("queryString")]
        public Output<string?> QueryString { get; private set; } = null!;

        /// <summary>
        /// The version of a Fleet Indexing query used by a fleet metric
        /// </summary>
        [Output("queryVersion")]
        public Output<string?> QueryVersion { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The unit of data points emitted by a fleet metric
        /// </summary>
        [Output("unit")]
        public Output<string?> Unit { get; private set; } = null!;

        /// <summary>
        /// The version of a fleet metric
        /// </summary>
        [Output("version")]
        public Output<double> Version { get; private set; } = null!;


        /// <summary>
        /// Create a FleetMetric resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FleetMetric(string name, FleetMetricArgs args, CustomResourceOptions? options = null)
            : base("aws-native:iot:FleetMetric", name, args ?? new FleetMetricArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FleetMetric(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iot:FleetMetric", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "metricName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing FleetMetric resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FleetMetric Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new FleetMetric(name, id, options);
        }
    }

    public sealed class FleetMetricArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The aggregation field to perform aggregation and metric emission
        /// </summary>
        [Input("aggregationField")]
        public Input<string>? AggregationField { get; set; }

        [Input("aggregationType")]
        public Input<Inputs.FleetMetricAggregationTypeArgs>? AggregationType { get; set; }

        /// <summary>
        /// The description of a fleet metric
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The index name of a fleet metric
        /// </summary>
        [Input("indexName")]
        public Input<string>? IndexName { get; set; }

        /// <summary>
        /// The name of the fleet metric
        /// </summary>
        [Input("metricName", required: true)]
        public Input<string> MetricName { get; set; } = null!;

        /// <summary>
        /// The period of metric emission in seconds
        /// </summary>
        [Input("period")]
        public Input<int>? Period { get; set; }

        /// <summary>
        /// The Fleet Indexing query used by a fleet metric
        /// </summary>
        [Input("queryString")]
        public Input<string>? QueryString { get; set; }

        /// <summary>
        /// The version of a Fleet Indexing query used by a fleet metric
        /// </summary>
        [Input("queryVersion")]
        public Input<string>? QueryVersion { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The unit of data points emitted by a fleet metric
        /// </summary>
        [Input("unit")]
        public Input<string>? Unit { get; set; }

        public FleetMetricArgs()
        {
        }
        public static new FleetMetricArgs Empty => new FleetMetricArgs();
    }
}
