// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Connect.Outputs
{

    /// <summary>
    /// The evaluation form item.
    /// </summary>
    [OutputType]
    public sealed class EvaluationFormItem
    {
        /// <summary>
        /// The evaluation form question item
        /// </summary>
        public readonly Outputs.EvaluationFormQuestion? Question;
        /// <summary>
        /// The evaluation form section item
        /// </summary>
        public readonly Outputs.EvaluationFormSection? Section;

        [OutputConstructor]
        private EvaluationFormItem(
            Outputs.EvaluationFormQuestion? question,

            Outputs.EvaluationFormSection? section)
        {
            Question = question;
            Section = section;
        }
    }
}
