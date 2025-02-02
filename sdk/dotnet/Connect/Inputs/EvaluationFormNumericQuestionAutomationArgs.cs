// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Connect.Inputs
{

    /// <summary>
    /// The automation properties for the numeric question.
    /// </summary>
    public sealed class EvaluationFormNumericQuestionAutomationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The automation property name of the question.
        /// </summary>
        [Input("propertyValue", required: true)]
        public Input<Inputs.EvaluationFormNumericQuestionPropertyValueAutomationArgs> PropertyValue { get; set; } = null!;

        public EvaluationFormNumericQuestionAutomationArgs()
        {
        }
        public static new EvaluationFormNumericQuestionAutomationArgs Empty => new EvaluationFormNumericQuestionAutomationArgs();
    }
}
