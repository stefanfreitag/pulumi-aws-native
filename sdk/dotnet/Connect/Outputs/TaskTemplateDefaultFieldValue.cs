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
    /// the default value for the task template's field
    /// </summary>
    [OutputType]
    public sealed class TaskTemplateDefaultFieldValue
    {
        public readonly string DefaultValue;
        public readonly Outputs.TaskTemplateFieldIdentifier Id;

        [OutputConstructor]
        private TaskTemplateDefaultFieldValue(
            string defaultValue,

            Outputs.TaskTemplateFieldIdentifier id)
        {
            DefaultValue = defaultValue;
            Id = id;
        }
    }
}
