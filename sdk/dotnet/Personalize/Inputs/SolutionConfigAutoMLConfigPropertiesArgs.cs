// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Personalize.Inputs
{

    /// <summary>
    /// The AutoMLConfig object containing a list of recipes to search when AutoML is performed.
    /// </summary>
    public sealed class SolutionConfigAutoMLConfigPropertiesArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The metric to optimize.
        /// </summary>
        [Input("metricName")]
        public Input<string>? MetricName { get; set; }

        [Input("recipeList")]
        private InputList<string>? _recipeList;

        /// <summary>
        /// The list of candidate recipes.
        /// </summary>
        public InputList<string> RecipeList
        {
            get => _recipeList ?? (_recipeList = new InputList<string>());
            set => _recipeList = value;
        }

        public SolutionConfigAutoMLConfigPropertiesArgs()
        {
        }
        public static new SolutionConfigAutoMLConfigPropertiesArgs Empty => new SolutionConfigAutoMLConfigPropertiesArgs();
    }
}
