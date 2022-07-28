// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RoboMaker
{
    /// <summary>
    /// AWS::RoboMaker::RobotApplication resource creates an AWS RoboMaker RobotApplication. Robot application can be used in AWS RoboMaker Simulation Jobs.
    /// </summary>
    [AwsNativeResourceType("aws-native:robomaker:RobotApplication")]
    public partial class RobotApplication : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The revision ID of robot application.
        /// </summary>
        [Output("currentRevisionId")]
        public Output<string?> CurrentRevisionId { get; private set; } = null!;

        /// <summary>
        /// The URI of the Docker image for the robot application.
        /// </summary>
        [Output("environment")]
        public Output<string?> Environment { get; private set; } = null!;

        /// <summary>
        /// The name of the robot application.
        /// </summary>
        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        [Output("robotSoftwareSuite")]
        public Output<Outputs.RobotApplicationRobotSoftwareSuite> RobotSoftwareSuite { get; private set; } = null!;

        /// <summary>
        /// The sources of the robot application.
        /// </summary>
        [Output("sources")]
        public Output<ImmutableArray<Outputs.RobotApplicationSourceConfig>> Sources { get; private set; } = null!;

        [Output("tags")]
        public Output<Outputs.RobotApplicationTags?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a RobotApplication resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RobotApplication(string name, RobotApplicationArgs args, CustomResourceOptions? options = null)
            : base("aws-native:robomaker:RobotApplication", name, args ?? new RobotApplicationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private RobotApplication(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:robomaker:RobotApplication", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing RobotApplication resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RobotApplication Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new RobotApplication(name, id, options);
        }
    }

    public sealed class RobotApplicationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The revision ID of robot application.
        /// </summary>
        [Input("currentRevisionId")]
        public Input<string>? CurrentRevisionId { get; set; }

        /// <summary>
        /// The URI of the Docker image for the robot application.
        /// </summary>
        [Input("environment")]
        public Input<string>? Environment { get; set; }

        /// <summary>
        /// The name of the robot application.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("robotSoftwareSuite", required: true)]
        public Input<Inputs.RobotApplicationRobotSoftwareSuiteArgs> RobotSoftwareSuite { get; set; } = null!;

        [Input("sources")]
        private InputList<Inputs.RobotApplicationSourceConfigArgs>? _sources;

        /// <summary>
        /// The sources of the robot application.
        /// </summary>
        public InputList<Inputs.RobotApplicationSourceConfigArgs> Sources
        {
            get => _sources ?? (_sources = new InputList<Inputs.RobotApplicationSourceConfigArgs>());
            set => _sources = value;
        }

        [Input("tags")]
        public Input<Inputs.RobotApplicationTagsArgs>? Tags { get; set; }

        public RobotApplicationArgs()
        {
        }
        public static new RobotApplicationArgs Empty => new RobotApplicationArgs();
    }
}
